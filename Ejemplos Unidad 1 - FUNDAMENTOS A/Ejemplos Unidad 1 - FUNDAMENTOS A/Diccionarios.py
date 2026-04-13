# ==========================================
# GUÍA RÁPIDA DE DICCIONARIOS EN PYTHON
# ==========================================

# 1. DECLARACIÓN (Crear el diccionario)
# Se usan llaves {} y la estructura es "llave": "valor"
usuario = {
    "nombre": "Mateo",
    "nivel": 25,
    "es_admin": True
}

print(f"Diccionario inicial: {usuario}")


# 2. ACCEDER A LOS DATOS
# En lugar de números (índices), usas la llave entre corchetes []
print(f"El nombre es: {usuario['nombre']}")

# TIP: Si usas .get(), el programa no se rompe si la llave no existe
print(f"Rango: {usuario.get('rango', 'No asignado')}")


#¿POR QUÉ NO SE USA EL PUNTO EN DICCIONARIOS?
# En Python, el punto (.) se reserva para acceder a MÉTODOS y ATRIBUTOS de un objeto.
# Por ejemplo, para usar el método de limpiar el diccionario:
# usuario.clear()  <-- Aquí sí se usa el punto porque .clear() es una función interna.


# 3. MODIFICAR Y AÑADIR
# Si la llave existe, se cambia el valor. Si no existe, se crea.
usuario["nivel"] = 26       # Modificar
usuario["ciudad"] = "Apure" # Añadir una nueva llave:valor

print(f"Diccionario actualizado: {usuario}")


# 4. ELIMINAR ELEMENTOS
# .pop("llave") -> Elimina la pareja y te devuelve el valor
ciudad_borrada = usuario.pop("ciudad")

# del -> Elimina directamente
del usuario["es_admin"]

print(f"Diccionario tras eliminar: {usuario}")


# 5. EXTRAS ÚTILES
# Ver solo las llaves, solo los valores o ambos
print(f"Llaves disponibles: {list(usuario.keys())}")
print(f"Valores guardados: {list(usuario.values())}")

# ¿Cuántas parejas hay?
print(f"Total de datos: {len(usuario)}")

# ==========================================
# Las llaves deben ser únicas (no puedes 
# tener dos "nombre"). Son ideales para 
# organizar datos de forma lógica.
# ==========================================