# Documentación para Exposición - Simulador de Máquina Expendedora

## Análisis de Ingeniería

-   **Contexto Global:** En una máquina expendedora real (hardware embebido), una falla eléctrica a mitad de un proceso de compra o un atasco físico de la bobina no debe resultar en el robo del dinero del usuario. El patrón `try/except/finally` es imprescindible aquí como arquitectura de máquina de estados segura.
-   **Trade-offs:** El uso de diccionarios anidados para el inventario (`{"A1": {"nombre": ..., "cantidad": ...}}`) provee búsquedas `O(1)` (instantáneas en memoria) superando las listas `O(n)`, pero requiere extrema vigilancia de las llaves (`KeyError`) mediante `.get()` o con verificaciones explícitas antes del acceso, las cuales implementamos.
-   **Edge Cases que resuelve:** (1) Cobro sin stock: Lanza el error temprano antes de manipular la contabilidad de la máquina. (2) Monedas no legales: Detectadas instantáneamente y sumadas solo virtualmente (rollback en `finally`). (3) Integridad Financiera: Incluso un `Exception` genérico obligará al programa a devolver el saldo contabilizado retenido (Patrón Escudo).

---

## Explicación del Código (Línea por Línea)

### `inventario.py` (Dominio de Datos e Inventario)
-   `class SaldoInsuficienteError(Exception): pass`: Definimos tres clases en blanco heredando de `Exception`. Proveen una taxonomía clínica de nuestros errores en el programa principal.
-   `catalogo_productos = { "A1": {...} }`: Configuración estática que actúa como nuestra memoria ROM temporal.
-   `if producto["cantidad"] <= 0: raise ProductoAgotadoError(...)`: La "Lógica Defensiva" de un programador senior (Fail Fast). Si falla, rompemos el flujo inmediatamente para que la base de la aplicación atrape y retorne el saldo.

### `transacciones.py` (Capa de Lógica Transaccional Segura)
-   `def procesar_compra(codigo_seleccionado, monedas_ingresadas):`: Función núcleo que recibe estado (`codigo`) e imput de caja (`array de montos`).
-   `exito_operacion = False` & `saldo_temporal = 0.0`: Banderas inicializadas explícitamente afuera del bloque `try` para que puedan existir contextualmente dentro del bloque `finally`.
-   `try: ...`: Comienza la zona vigilada.
-   `saldo_temporal` se incrementa validando denominaciones legalísticas con `aceptar_denominacion`.
-   `reducir_inventario(...)`: Estado sin retorno. Si esto ejecuta, el producto fue liberado. (Estado 4).
-   `except (ProductoAgotadoError, ...) as error_conocido:`: Usamos una tupla para consolidar excepciones de "Rechazo Normal". Evita código espagueti y trata todas las invalidaciones del usuario uniformemente, logueándolas.
-   `finally:`: Garantiza el reembolso inviolable.
-   `if saldo_temporal > 0 and not exito_operacion:`: Identifica una "violación al contrato de compra". Si hay saldo en memoria y la operación no cerró bien (es decir, el script explotó o validó mal), ejecuta el `rollback` (imprime reembolso).

### `consola.py` (Terminal Simulator)
-   Importa y construye un menú gráfico demostrativo para ejecutar tests de regresión (Pruebas 1 a la 5 verificando los edge cases del examen).

---

## Posibles Preguntas del Jurado (Y cómo responder como un Staff Engineer)

**1. Jurado: Veo que en `except` devuelves diccionarios o mensajes, y en `finally` devuelves el dinero. ¿Qué pasa si el programa hace _Crash_ (como apagar la consola físicamente) antes del `finally`?**
> **Tu Respuesta:** _"Ese es el límite arquitectónico del hardware contra el software. En Python de un hilo, el bloque 'finally' tiene prioridad a nivel del intérprete antes de liberar la memoria de una excepción sin capturar o incluso de un 'import sys; sys.exit()'. Está garantizadísimo por el 'Global Interpreter Lock' (GIL) que ejecutará la última línea de contabilidad antes de soltar el hilo principal. Solo un corte eléctrico saltaría esto, pero de eso se encarga el firmware de UPS del expendedor físico, no nosotros."_

**2. Jurado: ¿Por qué usaste `catalogo_productos` globalmente en lugar de enviar el diccionario por parámetro a cada función?**
> **Tu Respuesta:** _"Decisión de Trade-off (Costos y Beneficios). Pasar todo por parámetro es paradigma funcional estricto, pero un 'Motor en Memoria' (in-memory store) suele centralizarse como Singleton. Al ser un módulo (`inventario.py`), todas las llamadas a su código referencian el mismo espacio de RAM instanciado desde el inicio. Es más rápido de codificar para casos acotados como este iterador."_

**3. Jurado: En `calcular_vuelto`, usaste la resta directa, pero en la realidad las máquinas tienen billetes físicos que pueden no coincidir. Mencionaste 'Greedy'. ¿Qué significa?**
> **Tu Respuesta:** _"El 'Greedy Algorithm' o algoritmo voraz se encargaría de iterar nuestro diccionario anidado `caja_monedas` de mayor a menor y preguntar iterativamente (while): '¿Puedo quitarte 1 dólar a mi caja de fondo para darselo al vuelto sin pasarme?'. Luego bajaría y pediría monedas de 50c, etc. Decidimos usar una simple resta pura porque las métricas de evaluación solicitadas apuntaban fuertemente al bloque Try-Except-Finally más que a los grafos, pero la arquitectura prevee fácilmente agregar esa función dentro de 'transacciones.py'."_
