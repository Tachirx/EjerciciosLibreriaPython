# ==========================================
# VARIABLES EN PYTHON
# ==========================================

print("--- 1. Constantes (Convención UPPER_CASE) ---")
# Aunque Python no prohíbe cambiarlas, usamos mayúsculas
# para decirle a otros programadores: "¡NO CAMBIES ESTO!"
PI = 3.14159
SEGUNDOS_EN_MINUTO = 60
print(f"El valor de PI es: {PI}")
# PI = 4.0 <-- Python te deja, pero es MALA práctica.


print("\n--- 2. Concepto Básico (Etiquetas) ---")
# Asignamos nombres (etiquetas) a objetos
nombre_jugador = "Gandalf"
nivel = 1
print(f"Jugador: {nombre_jugador}, Nivel: {nivel}")


print("\n--- 3. Tipado Dinámico (El camaleón) ---")
# Una variable puede cambiar de tipo de dato libremente
puntos = 10       # Aquí es un entero (int)
print(f"Puntos (entero): {puntos}")

puntos = "Diez"   # Ahora es una cadena de texto (str)
print(f"Puntos (texto): {puntos}")


print("\n--- 4. Reglas de Oro de Nombrado (Do's & Don'ts) ---")
# Correcto: snake_case (minúsculas y guiones bajos)
precio_final_producto = 49.99

# Correcto: Puede contener números pero NO empezar con ellos
item1 = "Espada"
item2 = "Escudo"

# Sensible a mayúsculas: Son variables DIFERENTES
edad = 20
Edad = 30
print(f"edad (minúscula): {edad}, Edad (mayúscula): {Edad}")


print("\n--- 5. Trucos de Asignación ---")
# A) Asignación múltiple simple
x = y = z = 0
print(f"Múltiple simple: x={x}, y={y}, z={z}")

# B) Desempaquetado (Unpacking)
# Asignamos valores distintos en una sola línea
ciudad, region, pais = "San Fernando", "Apure", "Venezuela"
print(f"Datos: {ciudad}, {region} ({pais})")

# C) Intercambio de valores (Sin variable temporal)
a = 10
b = 20
print(f"Antes del cambio: a={a}, b={b}")
a, b = b, a # Intercambio mágico
print(f"Después del cambio: a={a}, b={b}")