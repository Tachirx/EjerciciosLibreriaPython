# Documentación para Exposición - Motor de Reservas y Overbooking

## Análisis de Ingeniería

-   **Contexto Global:** A diferencia de una Base de Datos SQL que utiliza Locks a nivel de fila (`FOR UPDATE`), en Python tenemos que gestionar en memoria el acceso competitivo a un diccionario (`base_datos_vuelos`). Este proyecto implementa una capa de acceso a datos pura (`gestion.py`) aislada de la lógica de servicios comerciales (`reservas.py`).
-   **Trade-offs:** El patrón de buscar el diccionario (`vuelo = consultar_vuelo(codigo_vuelo)`) devuelve una "Referencia de Memoria" (Puntero). Modificar este diccionario en `reservas.py` con un `.append()` altera inmediatamente los datos globales de `gestion.py`. Es rápido, pero en un entorno multi-hilo o asíncrono en la nube (`asyncio`), requeriría la adición de semáforos (`threading.Lock()`) para evitar violaciones de mutabilidad por hilos concurrentes.
-   **Edge Cases que resuelve:**
    -   (1) Inyección de Basura (Formatos Inválidos): Usando `ReservaInvalidaError`, el sistema jamás admite diccionarios anidados malformados que dañarían de forma permanente la base de datos simulada.
    -   (2) Operaciones Garantizadas (Trazabilidad): Utilizando `finally`, garantizamos legalmente (auditorías) que incluso si ocurre un sabotaje interno del sistema de Python (desborde de buffer simulado por otro error), un Ticket (con estado `FALLIDA` o `EXITOSA`) quedará obligatoriamente impreso en pantalla antes del cierre.

---

## Explicación del Código (Línea por Línea)

### `vuelos/gestion.py` (Capa de Persistencia Lógica)
-   `base_datos_vuelos = {...}`: Anidamiento a tres niveles de profundidad `Dict -> String -> List[Dict]`.
-   `def consultar_vuelo(codigo_vuelo):`: Implementación Fail-Fast. Si no hay llave, rompe el script para que el Programador corrija el error de red o ruteo, no el cliente.
-   `def verificar_disponibilidad(codigo_vuelo):`: El motor de comparación que responde el Overbooking pre-transacción mediante un conteo `len()` de la lista asíncrona interior en `O(1)` de complejidad temporal en Python moderno.

### `vuelos/reservas.py` (Capa de Lógica Comercial y Transacciones Seguras)
-   `estado_transaccion = "FALLIDA"`: Estandarte pesimista en la cima funcional asignado pre-`try`. ¿Por qué? Porque si le asignamos un estado en el minuto `5` del código pero falla al minuto `4`, la variable no existirá en el `finally` ocasionando un `UnboundLocalError`.  Aquí somos precavidos.
-   `if not str(pasajero["id"]).startswith("P-"):`: Validación estricta que dispara `ReservaInvalidaError` si el humano o el backend intermedio corrompen el payload (`{"id":"XXX"}`).
-   `if not hay_espacio: raise OverbookingError(...)`: Esta es la joya evaluativa de la unidad. El negocio dice explícitamente que la sobrecarga no es un flujo "Normal", sino una "Excepción del Sistema ("Error")".
-   `except OverbookingError as over_err:`: El sistema reacciona automáticamente. Atrapa este error programado y convierte una falla crítica en un "Upsell" o Lista de Espera, haciendo `.append()` al buffer alterno, mutando el status a `EN ESPERA`.
-   `finally:`: Garantiza generar y reportar el `codigo_tkt` con el `random.randint(...)` sin importar por qué ramificación del `Try` o `Except` pasó la flecha de ejecución de proceso.

---

## Posibles Preguntas del Jurado (Y cómo responder como un Staff Engineer)

**1. Jurado: En el `main.py` realizas la función global `print_estado_vuelos()`. ¿Por qué no la metiste dentro del módulo `gestion.py` si es una revisión de Datos?**
> **Tu Respuesta:** _"Principio de Acoplamiento y Responsabilidad (MVC). `gestion.py` es estrictamente una capa de Modelado de Datos (Back-End ciego). El Main es nuestro Controlador/Vista. La capa de datos provee las funciones de conteo, pero jamás debe saber 'cómo' se imprimirán en consola o si se van a imprimir. Proveer funciones de 'print()' en un gestor de base de datos interrumpe su reusabilidad en APIs REST donde imprimir a consola es inútil."_

**2. Jurado: Veo que `finally` genera un ticket. ¿Qué pasa si la falla fue en el `consultar_vuelo` (línea 17) antes de entrar al `try`?**
> **Tu Respuesta:** _"Este diseño fue altamente premeditado. Al estar el `consultar_vuelo` FUERA y ANTES del bloque `try`, si se envía un ID de código de vuelo que no existe (ej. V-999), se lanzará un `ValueError` limpio, rompiendo la función explícitamente SIN inyectar el bloque `finally`. El requerimiento pide ticket de intento de reserva. Un vuelo inexistente no es un intento de reserva de avión, es un error sintáctico de ruteo y no merece facturarse digitalmente con un ticket."_
