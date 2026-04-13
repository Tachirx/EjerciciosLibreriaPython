# Proyecto: Plataforma de Gestión de Editorial y Librería

Repositorio correspondiente al ejercicio práctico de algoritmos de ordenamiento, filtrado y transformación de diccionarios en Python. El sistema automatiza el cálculo de regalías y agrupa la data final para la interfaz web.

## Descripción del Flujo de Ejecución

El código en `gestion_libreria.py` se estructuró a través de tres fases lógicas, manteniendo consistencia y limpieza:

1. **Limpieza e Indexación (Parte A):** Iteración sobre el catálogo para descartar registros corruptos (sin ISBN) o inactivos (descatalogados). Genera un diccionario rápido agrupado por el ISBN.
2. **Cálculo de Regalías (Parte B):** Análisis focalizado en los libros del mercado de "Ficción" y "Académico". El sistema procesa de forma segura los valores numéricos y proyecta las regalías (`ventas * precio * porcentaje`). Los resultados se ordenan de mayor a menor ingreso.
3. **Agrupación para la Interfaz Web (Parte C):** Transforma la lista plana y reestructura el contenido indexándolo por el "género literario". Para evitar fallos semánticos (redundancia de llaves), se mutó la llave origen en el hijo y se inyectaron dinámicamente insignias tipo *Bestseller* dependiendo del histórico de ventas.

## Ejecución Local

1. Asegúrate de tener **Python 3.7+** instalado.
2. Clona el repositorio.
3. Posiciónate en la terminal dentro de la carpeta del proyecto.
4. Ejecuta el archivo principal:
   ```powershell
   python gestion_libreria.py
   ```
5. Podrás ver en consola la salida formateada con `json.dumps()` y se autogenerará físicamente el archivo `vista_libreria.json`.

## Manejo de Excepciones
El script contempla la posibilidad de datos corruptos mediante sentencias seguras `try-except` para fallos nativos de `ValueError` y `TypeError`, dotando de invulnerabilidad a las ecuaciones clave del cálculo de ingresos.

--- 
*Desarrollado para el análisis y evaluación de procesos internos algorítmicos.*
