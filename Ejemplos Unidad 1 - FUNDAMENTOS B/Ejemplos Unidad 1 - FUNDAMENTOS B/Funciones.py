# ==========================================================
# GUIA DE FUNCIONES EN PYTHON
# ==========================================================

# 1. FUNCIÓN DECLARADA, RETORNO Y ARGUMENTOS POR DEFECTO
# ----------------------------------------------------------
def crear_mensaje(usuario, plataforma="Web", version=1.0):
    """
    Demuestra parámetros obligatorios, por defecto y retorno de f-strings.
    """
    # El return puede devolver cualquier objeto (aquí una cadena formateada)
    return f"Hola {usuario}, bienvenido a {plataforma} (v{version})"

print("--- 1. Básicos ---")
print(crear_mensaje("Alex"))                    # Usa valores por defecto
print(crear_mensaje("Santi", "Android", 2.5))   # Sobrescribe valores


# 2. PROFUNDIZANDO EN *args (Argumentos Posicionales Variables)
# ----------------------------------------------------------
def calcular_promedio(nombre_clase, *notas):
    """
    *args captura todos los números en una TUPLA llamada 'notas'.
    """
    if not notas:
        return f"{nombre_clase}: No hay notas registradas."
    
    promedio = sum(notas) / len(notas)
    return f"Promedio en {nombre_clase}: {promedio:.2f}"

print("\n--- 2. *args ---")
# Caso A: Pasando argumentos uno por uno
print(calcular_promedio("Matemáticas", 10, 8, 9, 7))

# Caso B: Desempaquetando una lista (Importante)
mis_notas = [9, 10, 10, 8]
print(calcular_promedio("Física", *mis_notas)) # El '*' rompe la lista en pedazos individuales


# 3. PROFUNDIZANDO EN **kwargs (Argumentos de Clave-Valor)
# ----------------------------------------------------------
def generar_factura(cliente, **detalles):
    """
    **kwargs captura argumentos nombrados en un DICCIONARIO llamado 'detalles'.
    """
    print(f"Factura para: {cliente}")
    for item, precio in detalles.items():
        print(f"- {item}: ${precio}")

print("\n--- 3. **kwargs ---")
# Caso A: Pasando nombres directamente
generar_factura("Empresa ACME", Laptop=1200, Mouse=25, Teclado=50)

# Caso B: Pasando un diccionario existente (Desempaquetado con **)
compra_juan = {"Monitor": 300, "Cables": 15, "Silla": 150}
generar_factura("Juan Pérez", **compra_juan)


# 4. FUNCIONES LAMBDA (Casos de uso reales)
# ----------------------------------------------------------
# Son útiles para operaciones rápidas, como ordenar una lista de tuplas

# Una sola línea: lambda [argumentos] : [expresión]
print("\n--- 4. Lambdas ---")

doble = lambda x: x * 2

print(f"5. Lambda (doble de 8): {doble(8)}")

productos = [("Camisa", 20), ("Pantalón", 50), ("Gorra", 15)]

# Ordenar por precio (el segundo elemento de la tupla index 1)
productos_ordenados = sorted(productos, key=lambda p: p[1])

print(f"Productos ordenados por precio: {productos_ordenados}")

# Otro ejemplo: Lambda para calcular IVA rápidamente
calcular_iva = lambda precio: precio * 0.16
print(f"IVA de 100: {calcular_iva(100)}")


# 5. FUNCIONES DECLARADAS VS. EXPRESADAS
# ----------------------------------------------------------
print("\n--- 5. Declaradas vs Expresadas ---")

# Declarada: Existe formalmente con su nombre
def operacion_restar(a, b):
    return a - b

# Expresada: Guardamos la lógica (o la función entera) en una variable
# Esto las hace dinámicas (puedes pasar 'mi_herramienta' como argumento a otra función)
mi_herramienta = operacion_restar 

print(f"Usando función expresada: {mi_herramienta(20, 5)}")

# También podemos expresar una lógica condicional
es_par = lambda n: n % 2 == 0
print(f"¿Es 10 par?: {es_par(10)}")