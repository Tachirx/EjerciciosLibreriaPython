# Guía Técnica de Defensa — Calculadora de Gastos de Viaje Grupal

---

## ¿Qué resuelve este programa?

Cuando un grupo de amigos viaja juntos, cada persona paga montos distintos (hotel, comida, transporte, etc.). Al final del viaje surge la pregunta: **¿cuánto debe poner o recibir cada quien para que todos hayan gastado lo mismo?**

Este programa automatiza ese cálculo. Recibe los nombres y montos pagados, calcula el promedio justo, y muestra quién debe dinero y quién tiene saldo a favor.

---

## Arquitectura del Proyecto

El proyecto se divide en **tres archivos**, cada uno con una responsabilidad clara:

| Archivo | Responsabilidad |
|---|---|
| `calculos.py` | Contiene toda la lógica matemática: sumar, promediar y generar balances. |
| `interfaz.py` | Se encarga exclusivamente de **mostrar** los resultados en consola de forma visual. |
| `main.py` | Es el **punto de entrada**. Conecta la lógica con la interfaz y maneja los errores. |

Esta separación se llama **Separación de Responsabilidades**. La lógica de negocio (`calculos.py`) no imprime nada en pantalla, y la interfaz (`interfaz.py`) no hace ningún cálculo. Si en el futuro quisiéramos conectar este programa a una app móvil, solo cambiaríamos `interfaz.py` sin tocar la lógica.

---

## Explicación de `calculos.py`

Este archivo es el **cerebro matemático** del programa. Contiene tres funciones:

### Función `sumar_total`

```python
def sumar_total(participantes_pagos):
    return sum(participantes_pagos.values())
```

- Recibe un **diccionario** donde cada clave es el nombre de una persona y cada valor es el monto que pagó. Ejemplo: `{"Andres": 200, "Maria": 50}`.
- `participantes_pagos.values()` extrae únicamente los valores numéricos del diccionario: `[200, 50]`.
- `sum()` es una función nativa de Python que suma todos los elementos de una lista. En este caso devolvería `250`.

### Función `calcular_promedio`

```python
def calcular_promedio(total, cantidad_participantes):
    if cantidad_participantes == 0:
        raise ValueError("No hay participantes")
    return total / cantidad_participantes
```

- Recibe el `total` (la suma de todos los gastos) y la `cantidad_participantes` (cuántas personas hay en el grupo).
- **`if cantidad_participantes == 0:`** — Antes de dividir, verificamos que haya al menos una persona. Si la cantidad es cero, dividir cualquier número entre cero es una operación matemáticamente imposible. Por eso lanzamos el error de forma controlada.
- **`raise ValueError("No hay participantes")`** — La palabra `raise` significa "lanzar una excepción". `ValueError` es un tipo de error nativo de Python que indica que un valor recibido no es válido para la operación. El mensaje `"No hay participantes"` es el texto que verá el usuario.
- **`return total / cantidad_participantes`** — Si todo está bien, simplemente divide. Ejemplo: si el total fue `$400` y hay `4` personas, la cuota justa es `$100` por cabeza.

### Función `generar_balance`

```python
def generar_balance(participantes_pagos):
    cantidad = len(participantes_pagos)
    total_general = sumar_total(participantes_pagos)
    cuota_justa = calcular_promedio(total_general, cantidad)

    balances = {}
    for nombre, pagado in participantes_pagos.items():
        balances[nombre] = round(pagado - cuota_justa, 2)

    return total_general, cuota_justa, balances
```

Esta es la función **orquestadora**. Coordina las dos funciones anteriores y genera el resultado final.

- **`cantidad = len(participantes_pagos)`** — `len()` es una función nativa de Python que cuenta cuántos elementos tiene una estructura. Si el diccionario tiene 4 personas, `len()` devuelve `4`. Este valor se usa después para calcular el promedio.

- **`total_general = sumar_total(participantes_pagos)`** — Invoca nuestra primera función para obtener la suma total de gastos.

- **`cuota_justa = calcular_promedio(total_general, cantidad)`** — Invoca la segunda función. Si `cantidad` resultó ser `0`, aquí es donde se lanza el `ValueError` automáticamente.

- **`balances = {}`** — Se crea un **diccionario vacío**. En Python, las llaves `{}` representan un diccionario sin contenido. Lo usamos vacío porque será llenado dinámicamente dentro del bucle `for` que viene a continuación. Es como preparar una hoja de cálculo en blanco antes de empezar a escribir las filas.

- **`for nombre, pagado in participantes_pagos.items():`** — `items()` devuelve cada par clave-valor del diccionario original. En cada iteración del bucle, `nombre` toma el nombre de la persona y `pagado` toma el monto que aportó.

- **`balances[nombre] = round(pagado - cuota_justa, 2)`** — La operación central del programa:
  - Se resta la cuota justa a lo que pagó la persona.
  - Si pagó **más** que la cuota → el resultado es **positivo** (tiene dinero a favor, le deben).
  - Si pagó **menos** que la cuota → el resultado es **negativo** (debe dinero al grupo).
  - `round(..., 2)` redondea a 2 decimales para evitar errores de punto flotante como `$49.99999997`.
  - El resultado se guarda en el diccionario `balances` con el nombre de la persona como clave.

- **`return total_general, cuota_justa, balances`** — Devuelve tres valores empaquetados en una **tupla**: el gasto total, la cuota por persona, y el diccionario con el balance de cada integrante.

---

## Explicación de `interfaz.py`

Este archivo es la **capa visual**. Su única función es recibir los datos ya calculados y mostrarlos de forma legible.

```python
def formatear_recibo_general(total, promedio, balances):
    print("\n" + "="*50)
    print(f"       REPORTE FINANCIERO GRUPO DE VIAJE")
    print("="*50)
    print(f" Gasto Total del Viaje:           ${total:.2f}")
    print(f" Cuota Equitativa por Persona:    ${promedio:.2f}")
    print("-" * 50)
```

- Recibe los tres valores que devolvió `generar_balance`.
- `"="*50` repite el carácter `=` cincuenta veces para crear una línea decorativa.
- `f"${total:.2f}"` es una **f-string con formato numérico**: el `.2f` fuerza a que el número siempre se muestre con exactamente 2 decimales. Si `total` vale `400`, se imprime `$400.00`.

```python
    for persona, saldo in balances.items():
        if saldo > 0:
            print(f" [{persona:<10}] A FAVOR : Recibe  ${saldo:>6.2f}")
        elif saldo < 0:
            print(f" [{persona:<10}] EN DEUDA: Pagar   ${abs(saldo):>6.2f}")
        else:
            print(f" [{persona:<10}] AL DÍA  : Saldo    $0.00")
```

- Recorre el diccionario de balances.
- **`{persona:<10}`** — Alinea el texto a la **izquierda** en un espacio de 10 caracteres. Si el nombre es `"Ana"`, se rellena con espacios: `"Ana       "`. Esto crea columnas alineadas.
- **`{saldo:>6.2f}`** — Alinea el número a la **derecha** en un espacio de 6 caracteres con 2 decimales. Produce columnas numéricas prolijas.
- **`abs(saldo)`** — `abs()` devuelve el **valor absoluto** (elimina el signo negativo). Si el saldo es `-50`, `abs(-50)` devuelve `50`, permitiendo imprimir `Pagar $50.00` en vez de `Pagar $-50.00`.

---

## Explicación de `main.py`

Este archivo es el **controlador central** que une todo y maneja los errores.

### Importaciones

```python
from calculos import generar_balance
from interfaz import formatear_recibo_general
```

- `from calculos import generar_balance` — Trae la función orquestadora desde el archivo `calculos.py`. Python busca este archivo en la misma carpeta.
- `from interfaz import formatear_recibo_general` — Trae la función de impresión desde `interfaz.py`.

### Función `procesar_grupo`

```python
def procesar_grupo(participantes):
    print("Iniciando procesamiento de grupo...")
    try:
        total, promedio, balances = generar_balance(participantes)
        formatear_recibo_general(total, promedio, balances)

    except ValueError as val_err:
        print(f"\n[ERROR DE REQUISITO DE DISEÑO]: {val_err}")

    except ZeroDivisionError:
        print("\n[ALERTA DE MATEMÁTICA PURA]: Intento de división por cero detectado.")
        print("La lista de participantes está vacía. Abortando cálculo.")

    except Exception as e_general:
        print(f"\n[ERROR SISTÉMICO]: Ocurrió un fallo no previsto: {e_general}")
```

- **`try:`** — Abre un bloque protegido. Todo el código dentro será vigilado. Si algo falla, Python no se detiene: salta al bloque `except` correspondiente.
- **`total, promedio, balances = generar_balance(participantes)`** — Desempaqueta la tupla que devuelve `generar_balance` en tres variables separadas.
- **`except ValueError as val_err:`** — Si `calcular_promedio` detectó que no hay participantes y lanzó un `raise ValueError(...)`, Python salta directamente aquí. La variable `val_err` contiene el mensaje `"No hay participantes"`.
- **`except ZeroDivisionError:`** — Red de seguridad adicional. Si por alguna razón la validación del `ValueError` no se ejecutó y Python intentó dividir entre cero nativamente, este bloque lo atrapa.
- **`except Exception as e_general:`** — Captura cualquier otro error no anticipado. Es la última barrera de protección del sistema.

### Bloque de ejecución principal

```python
if __name__ == "__main__":
```

- Esta línea significa: "ejecuta todo lo de abajo **solo** si este archivo se corre directamente". Si otro archivo importara `main.py` como módulo, este bloque no se ejecutaría.

```python
    grupo_normal = {
        "Andres": 200,
        "Maria": 50,
        "Julio": 100,
        "Sofia": 50
    }
    procesar_grupo(grupo_normal)
```

- Se crea un diccionario con 4 amigos y sus gastos. El total es `$400`, la cuota justa es `$100`. Andrés pagó `$200`, así que tiene `$100` a favor. María y Sofía pagaron `$50`, así que cada una debe `$50`.

```python
    grupo_vacio = {}
    procesar_grupo(grupo_vacio)
```

- Se pasa un diccionario vacío (ningún participante). Esto deliberadamente provoca el `ValueError` dentro de `calcular_promedio`, demostrando que el sistema no se rompe.

```python
    try:
        res = sum([1, 2, 3]) / len([])
    except ZeroDivisionError as division_err:
        print(f"[RESCATE INTERNO] No puedes dividir {sum([1,2,3])} entre 0: {division_err}")
```

- Prueba aislada y directa del error `ZeroDivisionError`. `len([])` devuelve `0` porque la lista está vacía, y `6 / 0` dispara la excepción. El `except` la atrapa y muestra un mensaje descriptivo en vez de que el programa se detenga.

---

## Cómo ejecutar el programa

### Requisitos previos
- Tener **Python 3.6 o superior** instalado.
- Los tres archivos (`calculos.py`, `interfaz.py`, `main.py`) deben estar en la **misma carpeta**.

### Comando de ejecución

Abrir una terminal en la carpeta `4_gastos_viaje` y ejecutar:

```bash
python main.py
```

> **Nota:** Python es un lenguaje **interpretado**, no compilado. No se genera un `.exe`. El intérprete de Python lee el archivo `.py` línea por línea y lo ejecuta en tiempo real. Por eso se usa el comando `python` seguido del nombre del archivo.

### Salida esperada

```
=== TEST 1: Grupo de 4 Amigos (Funcionamiento Normal) ===
Iniciando procesamiento de grupo...

==================================================
       REPORTE FINANCIERO GRUPO DE VIAJE
==================================================
 Gasto Total del Viaje:           $400.00
 Cuota Equitativa por Persona:    $100.00
--------------------------------------------------
 [Andres    ] A FAVOR : Recibe  $100.00
 [Maria     ] EN DEUDA: Pagar   $ 50.00
 [Julio     ] AL DÍA  : Saldo    $0.00
 [Sofia     ] EN DEUDA: Pagar   $ 50.00
==================================================

=== TEST 2: Lista Vacía (Dispara ValueError) ===
Iniciando procesamiento de grupo...

[ERROR DE REQUISITO DE DISEÑO]: No hay participantes

=== TEST 3: Provocando el ZeroDivisionError de Sistema ===
[RESCATE INTERNO] No puedes dividir 6 entre 0: division by zero
```

---

## Conceptos clave que debes dominar para la defensa

| Concepto | Qué es | Dónde se usa |
|---|---|---|
| `dict` (Diccionario) | Estructura de datos que guarda pares `clave: valor` | `grupo_normal`, `balances` |
| `{}` vacío | Diccionario sin contenido, listo para llenarse | `balances = {}` en `calculos.py` |
| `len()` | Función nativa que cuenta los elementos de una estructura | `cantidad = len(participantes_pagos)` |
| `sum()` | Función nativa que suma los elementos de una lista | `sum(participantes_pagos.values())` |
| `round(x, 2)` | Redondea un número a 2 decimales | `round(pagado - cuota_justa, 2)` |
| `abs()` | Devuelve el valor absoluto (sin signo negativo) | `abs(saldo)` en `interfaz.py` |
| `raise` | Lanza una excepción manualmente | `raise ValueError("No hay participantes")` |
| `try/except` | Bloque protegido que atrapa errores sin detener el programa | `main.py` completo |
| `f-string` | Cadena con variables incrustadas usando `f"...{var}..."` | Todas las líneas de `print()` |
| `if __name__ == "__main__":` | Ejecuta el bloque solo si el archivo se corre directamente | Última sección de `main.py` |
