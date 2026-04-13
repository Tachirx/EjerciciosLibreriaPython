# ==========================================
# EL BUCLE FOR EN PYTHON: GUÍA DE ITERACIÓN
# ==========================================

# Ejemplo 1: Iterar sobre una LISTA
# Es la forma más común. Python toma un elemento a la vez.
frutas = ["manzana", "banana", "cereza"]
print("--- Ejemplo 1: Lista ---")
for fruta in frutas:
    print(f"Me gusta la {fruta}")


# Ejemplo 2: Iterar sobre una TUPLA
# Funciona exactamente igual que con las listas.
colores = ("rojo", "verde", "azul")
print("\n--- Ejemplo 2: Tupla ---")
for color in colores:
    print(f"Color: {color}")


# Ejemplo 3: Iterar sobre un DICCIONARIO
# Puedes iterar sobre llaves, valores o ambos.
usuario = {"nombre": "Mateo", "nivel": 25, "rol": "Admin"}
print("\n--- Ejemplo 3: Diccionario ---")
for clave, valor in usuario.items():
    print(f"{clave.capitalize()}: {valor}")

# ==========================================
# ITERACIÓN AVANZADA EN DICCIONARIOS
# ==========================================

# Nuestro diccionario de ejemplo
heroe = {
    "nombre": "Aragorn",
    "clase": "Guerrero",
    "nivel": 20,
    "reino": "Gondor"
}

# 1. ITERAR CON .keys()
# Se usa cuando solo te interesan las etiquetas (nombres de las categorías)
print("--- 1. Solo las Llaves (.keys()) ---")
for llave in heroe.keys():
    print(f"Propiedad: {llave}")


# 2. ITERAR CON .values()
# Se usa cuando solo te importa la información guardada, no el nombre de la etiqueta
print("\n--- 2. Solo los Valores (.values()) ---")
for valor in heroe.values():
    print(f"Dato: {valor}")


# 3. ITERAR CON .items() (La más completa)
# Te devuelve AMBAS cosas al mismo tiempo en cada vuelta del bucle. 
# Usamos dos variables: una para la llave y otra para el valor.
print("\n--- 3. Parejas Llave y Valor (.items()) ---")
for propiedad, detalle in heroe.items():
    print(f"{propiedad.upper()}: {detalle}")


# 4. CASO DE USO: Filtrar por valor
print("\n--- Bonus: Buscar valores específicos ---")
for k, v in heroe.items():
    if v == "Guerrero":
        print(f"¡Atención! El usuario tiene la clase: {v}")


# Ejemplo 4: Iterar sobre una CADENA DE TEXTO (String)
# Python trata a los strings como una colección de caracteres.
palabra = "Python"
print("\n--- Ejemplo 4: String ---")
for letra in palabra:
    print(f"Letra: {letra}")


# Ejemplo 5: Usando range() para repetir N veces
# range(inicio, fin_sin_incluir, salto)
print("\n--- Ejemplo 5: Range ---")
for i in range(3):
    print(f"Intento número {i + 1}")


# Ejemplo 6: Uso del BREAK y CONTINUE
# break: Detiene el bucle por completo.
# continue: Salta la iteración actual y pasa a la siguiente.
print("\n--- Ejemplo 6: Break y Continue ---")
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    if n == 2:
        continue # Salta el 2
    if n == 4:
        break    # Se detiene al llegar al 4
    print(f"Procesando número: {n}")