# ==========================================
# GUÍA RÁPIDA DE SETS (CONJUNTOS) EN PYTHON
# ==========================================

# 1. DECLARACIÓN (Crear el set)
# Se usan llaves {} pero SIN parejas de clave:valor
frutas = {"manzana", "pera", "uva", "manzana"} 

# NOTA: Aunque escribí "manzana" dos veces, Python solo guardará una.
print(f"Set inicial (sin duplicados): {frutas}")

# Para crear un set vacío DEBES usar set(), no {} (porque {} crea un diccionario)
vacio = set()

# 2. AÑADIR Y ELIMINAR
# .add() -> Añade un elemento
frutas.add("mango")

# .remove() -> Elimina un elemento (da error si no existe)
# .discard() -> Elimina un elemento (NO da error si no existe)
frutas.discard("pera")

print(f"Set tras modificar: {frutas}")


# 3. ACCESO (¡Cuidado!)
# Los sets NO tienen índice. No puedes hacer frutas[0].
# La forma de usarlos es recorriéndolos o preguntando si algo está dentro:
print(f"¿Hay uva?: {'uva' in frutas}")


# 4. OPERACIONES DE CONJUNTOS (Lo más potente)
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Unión (Juntar ambos sin repetir el 3)
print(f"Unión: {set_a | set_b}") # {1, 2, 3, 4, 5}

# Intersección (Solo los que están en AMBOS)
print(f"Intersección: {set_a & set_b}") # {3}

# Diferencia (Los que están en A pero no en B)
print(f"Diferencia: {set_a - set_b}") # {1, 2}


# 5. TRUCO MAESTRO: Limpiar listas
numeros_repetidos = [1, 2, 2, 3, 4, 4, 4, 5]
sin_repetir = list(set(numeros_repetidos))
print(f"Lista limpia: {sin_repetir}")

# ==========================================
# Usa sets cuando necesites asegurar que 
# un dato no se repita o cuando quieras 
# comparar dos grupos de datos rápidamente.
# ==========================================