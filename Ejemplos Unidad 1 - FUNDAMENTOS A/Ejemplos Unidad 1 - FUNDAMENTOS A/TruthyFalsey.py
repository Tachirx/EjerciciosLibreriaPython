def evaluar_valor(nombre, valor):
    # En Python, el 'if' evalúa si el objeto es Truthy o Falsy automáticamente
    if valor:
        print(f"{nombre} ({repr(valor)}) es TRUTHY")
    else:
        print(f"{nombre} ({repr(valor)}) es FALSY")

# --- Ejemplos de Valores FALSY ---
print("--- Probando Valores Falsy ---")
evaluar_valor("None", None)
evaluar_valor("Entero cero", 0)
evaluar_valor("Flotante cero", 0.0)
evaluar_valor("Cadena vacía", "")
evaluar_valor("Lista vacía", [])
evaluar_valor("Diccionario vacío", {})

print("\n--- Probando Valores Truthy ---")
# --- Ejemplos de Valores TRUTHY ---
evaluar_valor("Entero distinto de cero", 42)
evaluar_valor("Cadena con texto", "Hola Mundo")
evaluar_valor("Lista con elementos", [1, 2, 3])
evaluar_valor("Diccionario con datos", {"id": 1})
evaluar_valor("Espacio en blanco", " ") # Ojo pelao un espacio no es una cadena vacía

# --- Ejemplo de uso práctico ---
usuarios = []

if not usuarios:
    print("\nNo hay usuarios registrados")