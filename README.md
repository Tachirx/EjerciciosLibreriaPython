# Proyecto: Plataforma de Gestión de Editorial y Librería

Aquí alojamos nuestra solución de código para el ejercicio práctico de manipulación de datos en diccionarios de Python. Armamos un script que filtra datos, calcula ganancias y estructura todo al final para poder mostrarlo ordenado en una posible vista web.

## Descripción del Flujo de Ejecución

En el archivo `gestion_libreria.py` dividimos nuestro trabajo en tres fases claras para mantener todo limpio:

1. **Limpieza y Preparación (Parte A):** Pasamos por todo el catálogo inicial y descartamos aquellos libros incompletos (que no tuvieran la clave ISBN) o los que dijeran "descatalogado". Con la data buena que nos quedó, creamos un diccionario principal usando el ISBN como llave para buscar más rápido.
2. **Cálculo de Regalías (Parte B):** Filtramos solo las categorías que requiere el negocio ("Ficción" y "Académico"). Añadimos `try-except` para atrapar posibles errores de números vacíos o rotos en el archivo crudo y calculamos las regalías. Por último, ordenamos esa lista para dejar bien arriba a los que nos generen más plata.
3. **Agrupación para la Interfaz (Parte C):** Acomodamos nuestro listado agrupándolo de vuelta según el "género literario". Para no hacer código redundante, le borramos/mutamos esa misma llave al diccionario interno del libro, y en base a sus ventas le metimos dinámicamente una insignia ("Bestseller" o "Regular").

## Ejecución Local

1. **Python 3.7+ obligatorio**.
2. Clonar el repo en alguna carpeta para abrirlo.
3. Posiciónate en la terminal dentro de tu ruta del proyecto.
4. Lanza el código principal:
   ```powershell
   python gestion_libreria.py
   ```
5. Verás en pantalla el JSON resultante formateado súper claro y además soltará un propio archivo llamado `vista_libreria.json` para testear el guardado de datos.

--- 
*Evaluación - Lenguajes de Programación 2.*
