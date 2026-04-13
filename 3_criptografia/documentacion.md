# Documentación para Exposición - Analizador Criptográfico

## Análisis de Ingeniería

-   **Contexto Global:** A diferencia del uso de librerías de alto nivel (como `cryptography` o `base64`), este proyecto obliga a descender a nivel de bytes en memoria representando caracteres (`ord()` y `chr()`). La construcción matemática asegura que la tabla ASCII (128 caracteres base) se reduzca exclusivamente al margen alfabético (26 letras) usando aritmética modular estricta de base 64 (`A`) y 97 (`a`).
-   **Trade-offs:** Mapear y controlar mayúsculas y minúsculas independientemente, perdonando símbolos especiales (espacios y puntuación no se tocan), toma más ciclos de CPU (Branching constante en el bucle `if caracter.isalpha()`), pero preserva la legibilidad perfecta de la oración estructurada.
-   **Edge Cases que resuelve:** (1) Desbordamiento ASCII (Z +1 no se vuelve `[`, se vuelve `A` gracias al `% 26`). (2) Entradas tipográficas catastróficas del usuario atrapadas en la consola antes de inyectarlas al motor matemático (Bucle infinito de control con ValueError).

---

## Explicación del Código (Línea por Línea)

### `criptografia/__init__.py` (Encapsulamiento de Paquete)
-   `from .cesar import ...`: Convierte el directorio en un verdadero "módulo exportable". Cuando un desarrollador instale nuestro paquete, usará `import criptografia` directamente, ocultando la estructura de archivos interna.

### `criptografia/cesar.py` (Cálculo Lineal)
-   `desplazamiento = clave if cifrar else -clave`: Usando operador condicional (Ternary), usamos la misma función matemática para encriptar y reversar. Sumar la llave avanza. Restarla atrae.
-   `base_ascii = ord('A') if caracter.isupper() else ord('a')`: Determina la barrera inferior matemática. Las letras en memoria no arrancan en 0.
-   `nuevo_ascii = (ord(caracter) - base_ascii + desplazamiento) % 26 + base_ascii`:
    -   Restar la base (65) lleva la `"A"` a la posición algorítmica `0`.
    -   Se añade la llave (ej. `+5` = `5`).
    -   El módulo `% 26` limita a que si sumamos `27`, de una vuelta entera y termine en `1` (`B`).
    -   Sumamos de regreso el `+65` para poner el byte de regreso en un formato legible por pantalla y convertirlo con `chr()`.

### `criptografia/vigenere.py` (Cálculo Multiclave)
-   `letra_clave_actual = palabra_clave[clave_idx % longitud_clave]`: El secreto de Vigenère. En vez de desplazar el texto siempre por "3" iteraciones seguidas, se desplaza dependiendo del índice extraído de la palabra clave. Si la clave es `"SOL"` y el texto es `"ARBOL"`.
    -   A + S (Índice 0)
    -   R + O (Índice 1)
    -   B + L (Índice 2)
    -   O + S (Índice 3 - El módulo resetea la posición al inicio de "SOL").

### `main.py` (Manejo Estricto de Errores)
-   `def obtener_entero(mensaje):`: Una función wrapper defensiva.
-   `while True: try...`: El bucle infinito solo se romperá (`return`) si el tipado `int()` convierte exitosamente el texto que tipeó el usuario por teclado. Si el usuario tipea `"Gato"`, el _engine_ lanza `ValueError`, el `except` lo intercepta, imprime la corrección amablemente y el iterador regresa arriba, atrapando la mala acción del humano.

---

## Posibles Preguntas del Jurado (Y cómo responder como un Staff Engineer)

**1. Jurado: En Vigenère ¿Por qué lanzas un ValueError si la contraseña que introdujo el usuario tiene un número en lugar de pedirla de nuevo como lo hiciste en la consola?**
> **Tu Respuesta:** _"Separación del dominio de responsabilidad. La función `_procesar_vigenere` dentro del motor matemático (Back-End) no debe interactuar con el usuario. Si el motor falla, debe fallar ruidosamente (Raise Error). Es tarea del Front-End (`main.py` con sus bucles `while True`) atrapar las instrucciones de entrada no legales de los humanos. Pasan 2 niveles de validación: La pre-validación de vista, y la estricta del motor matematico."_

**2. Jurado: ¿Podrías cambiar el código para que encripte la 'ñ' y los espacios en blanco?**
> **Tu Respuesta:** _"Sí. Actualmente usamos módulo de 26 basado exclusívamente en el alfabeto inglés tradicional. Para incluir la Ñ y signos ortográficos, simplemente tendríamos que ampliar el espectro base, abandonar `ord('A')` y definir una cadena dura como `ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ '`. En lugar de sacar el Modulo 26, el desplazamiento se haría calculando el `.index()` de cada letra del texto contra el tamaño del `ALFABETO` total."_
