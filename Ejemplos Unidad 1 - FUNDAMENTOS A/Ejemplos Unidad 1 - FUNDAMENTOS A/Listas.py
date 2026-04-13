# 1. DECLARACIÓN (Crear la lista)
# Se usan corchetes [] y los elementos se separan por comas
frutas = ["manzana", "pera", "uva"]
numeros = [10, 20, 30]
vacia = []

print(f"Lista inicial: {frutas}")


# 2. ACCEDER Y MODIFICAR (Usando índices)
# IMPORTANTE: Python empieza a contar desde 0
primera = frutas[0]  # "manzana"
print(f"La primera fruta es: {primera}")

# Modificar un valor existente
frutas[1] = "mango"  # Cambiamos "pera" por "mango"
print(f"Lista tras modificar el índice 1: {frutas}")


# 3. AÑADIR ELEMENTOS
# .append() -> Añade siempre al FINAL
frutas.append("naranja")

# .insert(posicion, valor) -> Añade en un lugar específico
frutas.insert(1, "fresa") # La fresa ahora estará en la posición 1

print(f"Lista tras añadir elementos: {frutas}")


# 4. ELIMINAR ELEMENTOS
# .pop() -> Elimina el ÚLTIMO de la lista
frutas.pop() 

# .remove(valor) -> Busca el nombre y lo borra
frutas.remove("manzana")

print(f"Lista tras eliminar: {frutas}")


# 5. EXTRAS ÚTILES
# ¿Cuántos elementos hay?
total = len(frutas)

# ¿Está un elemento en la lista? (Devuelve True o False)
existe = "mango" in frutas

print(f"Total de frutas: {total}")
print(f"¿Hay mango?: {existe}")

# ==========================================
# Las listas son "mutables", lo que 
# significa que puedes transformarlas todo 
# lo que quieras mientras el programa corre.
# ==========================================