# ==========================================
# SENTENCIA MATCH
# ==========================================

# 1. USO BÁSICO (Como un Switch tradicional)
dia = "Lunes"

print("--- Ejemplo 1: Básico ---")
match dia:
    case "Lunes":
        print("Inicio de semana.")
    case "Viernes":
        print("Casi fin de semana.")
    case "Sábado" | "Domingo": # El símbolo | funciona como un "OR"
        print("Es fin de semana.")
    case _: # El guion bajo es el "default" (si nada de lo anterior coincide)
        print("Es un día laboral cualquiera.")


# 2. MATCH CON ESTRUCTURAS (Listas)
# El match puede "mirar" qué hay dentro de una lista
comando = ["move", "norte"]

print("\n--- Ejemplo 2: Listas ---")
match comando:
    case ["quit"]:
        print("Saliendo del juego...")
    case ["move", direccion]:
        print(f"Moviendo el personaje hacia el {direccion}.")
    case ["get", objeto, cantidad]:
        print(f"Recogiendo {cantidad} unidades de {objeto}.")
    case _:
        print("Comando no reconocido.")


# 3. MATCH CON DICCIONARIOS
# Útil para procesar datos de APIs o configuraciones
usuario = {"nombre": "Mateo", "rol": "admin"}

print("\n--- Ejemplo 3: Diccionarios ---")
match usuario:
    case {"rol": "admin"}:
        print("Acceso total concedido.")
    case {"rol": "editor", "nombre": nombre}:
        print(f"Bienvenido editor {nombre}, puedes modificar posts.")
    case {"nombre": nombre}:
        print(f"Hola {nombre}, tienes acceso limitado.")


# 4. USANDO "GUARDS" (Condiciones Extra)
# Puedes añadir un 'if' dentro del case para filtrar más fino
puntos = 15

print("\n--- Ejemplo 4: Con condiciones (Guards) ---")
match puntos:
    case n if n >= 10:
        print(f"¡Nivel Alto! Puntos: {n}")
    case n if n > 0:
        print(f"Nivel Bajo. Puntos: {n}")
    case _:
        print("Sin puntos.")

# 5. WILDCARD

boton_presionado = "TRIÁNGULO"

match boton_presionado:
    case "PLAY":
        print("Reproduciendo música...")
    case "PAUSE":
        print("Música pausada.")
    case _:
        # El WILDCARD captura cualquier cosa que no sea PLAY o PAUSE
        # (Como "TRIÁNGULO", "X", o cualquier error)
        print(f"El botón '{boton_presionado}' no hace nada en este menú.")