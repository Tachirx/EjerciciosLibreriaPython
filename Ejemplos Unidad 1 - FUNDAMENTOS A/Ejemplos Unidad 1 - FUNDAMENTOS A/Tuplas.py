# ==========================================
# TUPLAS EN PYTHON
# ==========================================

# 1. DECLARACIÓN (Crear la tupla)
# Se usan paréntesis () en lugar de corchetes
colores = ("rojo", "verde", "azul")
numeros = (1, 2, 3)
punto_gps = (7.889, -67.472) # Muy común para datos que no deben cambiar

# IMPORTANTE: Si quieres una tupla de UN solo elemento, lleva coma:
solo_uno = ("uno",) 

print(f"Tupla inicial: {colores}")


# 2. ACCEDER (Igual que las listas)
# Python empieza a contar desde 0
print(f"El primer color es: {colores[0]}")
print(f"El último color es: {colores[-1]}")


# 3. ¿SE PUEDEN MODIFICAR? (¡NO!)
# Si intentas hacer: colores[1] = "amarillo", Python dará ERROR.
# Las tuplas no tienen .append(), .insert() ni .pop()
print("\nNota: Las tuplas son inmutables (no se pueden cambiar).")


# 4. DESEMPAQUETADO (Unpacking)
# Una forma genial de pasar valores de una tupla a variables
r, v, a = colores
print(f"Variable r: {r}, Variable v: {v}, Variable a: {a}")


# 5. EXTRAS ÚTILES
# ¿Cuántos elementos hay?
total = len(colores)

# ¿Está un elemento en la tupla?
existe = "verde" in colores

# Contar cuántas veces aparece un valor
repeticiones = colores.count("rojo")

print(f"Total de elementos: {total}")
print(f"¿Existe el verde?: {existe}")

# ==========================================
# Usa tuplas cuando quieras proteger tus 
# datos de cambios accidentales o cuando 
# necesites una colección de datos fija.
# ==========================================