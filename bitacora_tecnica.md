# Bitácora Técnica

## Registro de Implementaciones y Mejoras

### 2026-03-23 20:30:15
- **Acción:** Planificación e Implementación Masiva de 5 Proyectos Evaluativos (Unidad 1 - Lenguajes de Programación 2).
- **Detalle:** Se implementó arquitectura modular siguiendo las reglas estrictas de Staff Engineer (Nomenclatura 100% español).
  1. Motor Elo con procesamiento por lotes.
  2. Expendedora con Máquina de Estados y `try/except/finally`.
  3. Criptografía Vigenère/César estructurada sin librerías de alto nivel.
  4. Gastos de viaje validando el desbordamiento matemático nativo (`ZeroDivisionError`).
  5. Vuelos en memoria simulando persistencia competitiva concurrente y Overbooking.
  Se acompañó cada directorio con su respectivo análisis explicativo `documentacion.md` para preparar el speech del jurado.

### 2026-03-19 20:47:16
- **Acción:** Creación de la estructura de investigación local (`analyzer.py`) para extraer datos de PDFs y ejercicios Python sin exceder la cuota de tokens.
- **Detalle:** Se implementó un script que procesa iterativamente los archivos locales, evitando enviar todo el contenido a través de la red (prompts masivos), resolviendo así la petición directa de eficiencia y ahorro de tokens.
### 2026-03-20 19:38:00
- **Acción:** Configuración de servidores MCP para VS Code.
- **Detalle:** Se han extraído los servidores `stitch`, `mysql`, `serper` y `filesystem` desde la configuración interna del agente y se han volcado en `.gemini/settings.json`, permitiendo su uso directo en VS Code mediante la extensión correspondiente.
### 2026-03-20 19:47:00
- **Acción:** Integración de instrucciones globales en el workspace de VS Code.
- **Detalle:** Se han copiado las reglas de comportamiento de `GEMINI.md` al archivo `.clinedules` en la raíz del proyecto para asegurar que las extensiones de IA en VS Code sigan los mismos protocolos que el agente original. También se creó `instructions.json` en `.gemini`.

### 2026-03-22 21:26:00
- **Acción:** Resolución de `Ejercicios1.py` (Unidad 1 - FUNDAMENTOS B).
- **Detalle:** Se implementaron las soluciones a los 7 ejercicios solicitados (Listas, Tuplas, Sets, While, For, Match), asegurando que el código sea 100% funcional y cumpliendo con la regla de establecer todas las variables y estructuras semánticas en español.

### 2026-03-22 21:38:00
- **Acción:** Elaboración de manual teórico detallado (`explicacion_ejercicios_1.md`).
- **Detalle:** Se generó una documentación estructurada y didáctica explicando semánticamente el flujo del script base (complejidad temporal de operadores, tipos de estructuras y comportamiento en memoria del motor de datos de Python).

### 2026-04-11 19:38:00
- **Acción:** Resolución de ejercicio: Plataforma de Gestión de Editorial y Librería.
- **Detalle:** Se implementó `gestion_libreria.py` abordando la limpieza de listas de diccionarios, cálculo de regalías y recategorización estructural (UI/Web) eliminando llaves anidadas y generando insignias dinámicas, asegurando nomenclatura íntegra en español.
