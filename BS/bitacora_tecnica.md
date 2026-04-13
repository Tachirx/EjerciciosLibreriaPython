# Bitácora Técnica de Implementaciones y Mejoras

## Registro de Cambios

**Fecha y Hora:** 2026-03-29 21:29:17 (Hora Local)
* **Componente:** `bloodstrike` (Radar Táctico V2).
* **Descripción:** 
  * Se reescribió la lógica para eliminar barras estáticas y evolucionar a un Radar HUD (Crosshair Overlay) centrado.
  * *DSP incorporado:* Implementación de Noise Gate dinámico mediante búferes circulares en memoria, evitando ruidos constantes en 200Hz.
  * *UI:* Interpolación Lineal (Lerp) manual para animaciones premium de desvanecimiento ("Fade-Out") sin bloquear la vista.
  * *Accesibilidad:* Registro asíncrono en Hilo de atajos globales `Ctrl+Flecha` a través de librería `keyboard` para modificar sensibilidad en vivo.
  * *Matemáticas:* Trigonometría básica por relación L/R para determinar ángulos de origen de sonido y dibujar Arcos Direccionales (QPainter Arc).
* **Patrón de Diseño:** Productor-Consumidor (Hilos), Interpolador Matemático Lineal, Suscripción a Eventos Asíncronos.
