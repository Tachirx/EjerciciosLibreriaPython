# Documentación para Exposición - Calculadora de Gastos de Viaje Grupal

## Análisis de Ingeniería

-   **Contexto Global:** Una herramienta cotidiana para resolver los flujos de "quien le debe a quien" después de un viaje. La clave matemática es comparar el "Total / n_participantes" contra el "Monto individual aportado". El patrón usado es arquitectónico: UI Pasiva (`interfaz.py` no procesa lógica, solo grafica) y Lógica Transparente (`calculos.py` no imprime nada en pantalla, solo retorna los saldos). 
-   **Trade-offs:** Usar un solo script `main` habría ahorrado importaciones y saltos de contexto. Sin embargo, diseñar `calculos.py` sin los comandos de `print()` asegura que si en el futuro queremos enlazar este módulo a un React/Flutter front-end, servirá sin modificaciones a través de una API.
-   **Edge Cases que resuelve:** "Lista Vacía" (`ZeroDivisionError`). Al intentar dividir cualquier cuenta de gastos del viaje entre 0 amigos, la matemática de Von Neumann produce una falta (Falla Grave de CPU). Las métricas estrictamente piden prevenir esto mediante un `ZeroDivisionError` en el `try/except` general, pero también levantando un `ValueError` preventivo en el core.

---

## Explicación del Código (Línea por Línea)

### `calculos.py` (Cerebro Matemático Sin Vista)
-   `def sumar_total(participantes_pagos):`: Usando diccionarios de entrada, `sum(participantes_pagos.values())` ejecuta el acumulador numérico en lenguaje binario directo (mucho más rápido que hacer un ciclo for `+=`).
-   `if cantidad_participantes == 0: raise ValueError("No hay participantes")`: Es la defensa prioritaria. Si no detectamos que la longitud del diccionario es 0, Python al ejecutar la siguiente línea lanzaría `ZeroDivisionError` irremediablemente.
-   `return total / cantidad_participantes`: Pura división.
-   `def generar_balance(participantes_pagos):`: Esta es la función orquestadora interior.  En un bucle for, calcula la resta entre el promedio (Cuota justa) y lo que realmente gastó el amigo. Si gastó `200` y la cuota era `100`, da `+100` (Recibe a favor).

### `interfaz.py` (Motor de Estilos de Vista)
-   `def formatear_recibo_general(total, promedio, balances):`: Usa las famosas F-Strings de Python 3 avanzadas.
-   `{persona:<10}`: Alineación izquierda, rellenando con espacios hasta lograr 10 caracteres. Esto asegura que todas las filas (columnas de la tabla en consola) salgan en perfecto alineamiento vertical.
-   `${abs(saldo):>6.2f}`: Alineación derecha en una columna de 6 caracteres con dos números decimales. `abs()` es crítico porque elimina el guion matemático del número negativo `-50` y permite a la interfaz escribir "PAGAR $50" de manera amigable.

### `main.py` (Inyector de Dependencias y Control de Errores)
-   `def procesar_grupo(participantes):`: Es la puerta del Back-end. Ingresa al `try`, extrae de `generar_balance` y lo manda a `formatear_recibo_general`.
-   `except ValueError as val_err:`: El Requerimiento principal de atrapar "No hay participantes".
-   `except ZeroDivisionError:`: La trampa de red de seguridad base para divisiones entre cero por cualquier otra causa ajena al diccionario inicial (Ej: si `len()` diera falso positivo).

---

## Posibles Preguntas del Jurado (Y cómo responder como un Staff Engineer)

**1. Jurado: En `calculos.py` tu método `calcular_promedio` lanza un ValueError que detiene el `ZeroDivisionError` antes de que ocurra. ¿Por qué el requerimiento pide ambos catchers?**
> **Tu Respuesta:** _"Se llama Defensa en Profundidad (Defense in Depth). Si alguien (otro desarrollador junior del equipo en 3 años) borra accidentalmente nuestro 'if cantidad == 0: raise ValueError', se reestablecerá el daño del 'ZeroDivisionError'. En sistemas de software, validamos la regla de negocio primero ('No hay participantes'), y validamos la regla electromatemática nativa después. Nuestro código demuestra conocer ambos mundos: La capa Dominio ('ValueError') y la capa Algorítmica ('ZeroDivisionError')."_

**2. Jurado: Veo que formateas usando `abs(saldo)`. ¿Por qué enviar números negativos desde cálculo a la interfaz?**
> **Tu Respuesta:** _"La base matemática (calculos.py) debe manejar invarianzas vectoriales exactas y puras (Positivo = Excedente, Negativo = Déficit). Así es como funciona cualquier motor financiero como Stripe o PayPal. La capa de Interfaz Gráfica (`interfaz.py`) es la que debe interpretar que un Humano no comprende fácilmente un 'Tu recibo es de $-50', por lo cual usa el Absoluto e imprime la palabra estática de negocio 'DEBE'."_
