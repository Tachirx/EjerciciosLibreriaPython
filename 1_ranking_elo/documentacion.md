# Documentación para Exposición - Motor de Cálculo de Ranking Elo

## Análisis de Ingeniería

-   **Contexto Global:** Este proyecto descentraliza la lógica de un sistema tradicional monolítico. `core_elo.py` se encarga exclusivamente de las matemáticas (puro y testeable estadísticamente sin dependencias). `datos.py` simula la capa de persistencia (Base de Datos o Memoria) mediante diccionarios, y el `procesador.py` funciona como el controlador transaccional que gestiona el procesamiento por lotes.
-   **Trade-offs:** La separación en módulos implica que la validación de la existencia de un jugador recaiga en `datos.py` a través de excepciones (`JugadorNoEncontradoError`). Esto añade verbosidad mediante bloques `try/except`, pero incrementa masivamente la mantenibilidad a largo plazo frente a enfoques rápidos de _"un solo archivo"_.
-   **Edge Cases que resuelve:** (1) Diccionario corrupto (Líneas con un separador de más o de menos que saltan IndexError). (2) Jugadores no encontrados. (3) Formatos inválidos saltados limpia y consistentemente. (4) Cálculos de probabilidad precisos (`factor_k` o `400` garantizan invariabilidad en los resultados ELO oficiales).

---

## Explicación del Código (Línea por Línea)

### `core_elo.py` (Fundamentos matemáticos)
-   `def calcular_nuevo_elo(elo_a, elo_b, resultado_a, factor_k=32):`: Firma de la función que recibe Elos y el multiplicador estándar del ajedrez (32 por defecto).
-   `esperanza_a = 1 / (1 + 10 ** ((elo_b - elo_a) / 400))`: Implementación matemática de la curva logística de probabilidad de ganar para el jugador A.
-   `resultado_b = 1 - resultado_a`: Si A gana (1), B pierde (0). Si A empata (0.5), B empata (1 - 0.5 = 0.5).
-   `nuevo_elo_a = elo_a + factor_k * (resultado_a - esperanza_a)`: Transforma la esperanza frente al resultado real en la nueva puntuación.
-   `return round(nuevo_elo_a, 2), round(nuevo_elo_b, 2)`: Retorna la tupla redondeada a dos decimales.

### `datos.py` (Capa de Persistencia)
-   `class JugadorNoEncontradoError(Exception): pass`: Excepción personalizada y amigable (semántica clara para el desarrollador de la capa procesadora).
-   `base_datos_jugadores = {...}`: Diccionario en memoria que almacena métricas (Elo y partidas).
-   `def obtener_jugador(nombre):`: Función que extrae del diccionario o lanza el `JugadorNoEncontradoError`.

### `procesador.py` (Lógica de Negocio y Bucle)
-   `def procesar_lote_partidas(lote_partidas):`: Ingresa una lista de strings simulando un archivo CSV o base de texto.
-   `for indice, linea in enumerate(lote_partidas):`: Itera sobre las líneas conociendo su posición.
-   `try: ...`: El bloque maestro transaccional para evitar crasheos que perjudiquen torneos completos.
-   `partes = [p.strip() for p in linea.split("|")]`: List comprehension que paralelamente recorta espacios en blanco en la cadena segmentada.
-   `except JugadorNoEncontradoError as error_jugador:`: Atrapa limpiamente el error para _skip()_ de esta línea continuando el bucle a las siguientes partidas reales.

---

## Posibles Preguntas del Jurado (Y cómo responder como un Staff Engineer)

**1. Jurado: ¿Por qué decidiste separar la fórmula matemática (`core_elo.py`) de la validación del lote (`procesador.py`) en lugar de poner todo en un ciclo for masivo?**
> **Tu Respuesta:** _"Se trata del principio de Responsabilidad Única (SRP) de SOLID. La formulación matemática es una entidad estática y absoluta; no necesita saber si un string está mal formateado o si el jugador existe en base de datos. Al tener `core_elo.py` separado, el día de mañana podría conectarlo a una API web sin tocar para nada el código de matemáticas, porque no tiene acoplamiento. Además, facilita aplicar pruebas unitarias (Unit Testing) puras."_

**2. Jurado: Veo que usaste `try/except` generalizado al final (except Exception). ¿No es eso una mala práctica para ocultar errores?**
> **Tu Respuesta:** _"Generalmente encubrir errores es mala práctica (`pass` silente). Sin embargo, en un procesador batch por lotes, la premisa de negocio es que un error en 1 partida de entre 10,000 no debe detener el sistema entero. Atrapé explícitamente `ValueError` y `JugadorNoEncontradoError` primero. Si ocurre un `Exception` genérico como un problema de memoria, registro la advertencia completa para los logs del servidor y obligo al sistema a sobrevivir para seguir procesando."_

**3. Jurado: ¿Qué pasaría si quisieramos llevar este proyecto de "memoria" a una Base de Datos Real SQL?**
> **Tu Respuesta:** _"Dado que la arquitectura ya está desacoplada, la lógica masiva del sistema (`core_elo` y el bucle del `procesador`) no cambiaría en absolutamente nada. Solo tendríamos que modificar las funciones dentro de `datos.py` (`obtener_jugador` y `actualizar_elo_jugador`) inyectando conectores SQL (ej. `pymysql` o `sqlalchemy`). Esto es el patrón Repository."_
