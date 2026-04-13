import json
from datetime import datetime

# --- Parte A: Limpieza e Indexación ---
def generar_catalogo_activo(lista_libros):
    """
    Filtra los libros descatalogados o sin ISBN.
    Retorna un diccionario indexado por ISBN y la cantidad de libros descartados.
    """
    diccionario_indice = {}
    cantidad_descartados = 0
    
    for libro in lista_libros:
        if "isbn" not in libro or libro.get("estado_impresion") == "descatalogado":
            cantidad_descartados += 1
            continue
            
        diccionario_indice[libro["isbn"]] = libro
        
    return diccionario_indice, cantidad_descartados

# --- Parte B: Análisis y Ordenamiento ---
def calcular_regalias_pendientes(indice_libros):
    """
    Calcula regalías, filtra por Ficción o Académico y ordena la lista final.
    Retorna una lista de diccionarios ordenados.
    """
    libros_filtrados = []
    
    for _, libro in indice_libros.items():
        if libro.get("categoria") in ("Ficción", "Académico"):
            try:
                ventas = float(libro.get("unidades_vendidas", 0))
                precio = float(libro.get("precio", 0.0))
                porcentaje = float(libro.get("porcentaje_autor", 0.0))
                
                libro["regalia_proyectada"] = ventas * precio * porcentaje
            except (ValueError, TypeError):
                libro["regalia_proyectada"] = 0.0
                
            libros_filtrados.append(libro)
            
    libros_filtrados.sort(
        key=lambda x: (-x.get("regalia_proyectada", 0), x.get("apellido_autor", ""))
    )
    
    return libros_filtrados

# --- Parte C: Agrupación para Interfaz Gráfica ---
def estructurar_vista_generos(indice_libros):
    """
    Agrupa los libros por género literario, asigna insignia web y 
    elimina la redundancia del género en cada elemento hijo.
    Retorna el diccionario agrupado.
    """
    iterable_libros = indice_libros.values() if isinstance(indice_libros, dict) else indice_libros
    vista_generos = {}
    
    for libro in iterable_libros:
        libro_vista = dict(libro)
        
        genero = libro_vista.get("genero_literario", "Sin Asignar")
        
        try:
            ventas = float(libro_vista.get("unidades_vendidas", 0))
        except (ValueError, TypeError):
            ventas = 0
            
        if ventas > 1000:
            libro_vista["insignia_web"] = "Bestseller"
        else:
            libro_vista["insignia_web"] = "Regular"
            
        if "genero_literario" in libro_vista:
            del libro_vista["genero_literario"]
            
        if genero not in vista_generos:
            vista_generos[genero] = []
            
        vista_generos[genero].append(libro_vista)
        
    return vista_generos

if __name__ == "__main__":
    # Estructura de pruebas - Lista cruda mockeada
    lista_libros = [
        {"isbn": "978-1", "titulo": "Cien Años de Soledad", "precio": 25.0, "unidades_vendidas": 1500, "stock": 40, "genero_literario": "Ficción", "apellido_autor": "García Márquez", "porcentaje_autor": 0.15, "estado_impresion": "activo", "categoria": "Ficción"},
        {"isbn": "978-2", "titulo": "Cálculo de Una Variable", "precio": 50.0, "unidades_vendidas": 500, "stock": 20, "genero_literario": "Matemáticas", "apellido_autor": "Stewart", "porcentaje_autor": 0.10, "estado_impresion": "activo", "categoria": "Académico"},
        {"isbn": "978-3", "titulo": "Libro Viejo", "precio": 10.0, "unidades_vendidas": 5, "stock": 2, "genero_literario": "Historia", "apellido_autor": "Desconocido", "porcentaje_autor": 0.05, "estado_impresion": "descatalogado", "categoria": "Ficción"}, 
        {"isbn": "978-4", "titulo": "1984", "precio": 18.0, "unidades_vendidas": 2000, "stock": 50, "genero_literario": "Ficción", "apellido_autor": "Orwell", "porcentaje_autor": 0.12, "estado_impresion": "activo", "categoria": "Ficción"},
        {"isbn": "978-5", "titulo": "Python para Todos", "precio": 35.0, "unidades_vendidas": 1200, "stock": 100, "genero_literario": "Programación", "apellido_autor": "Severance", "porcentaje_autor": 0.20, "estado_impresion": "activo", "categoria": "Académico"}, 
        {"titulo": "Libro sin ISBN", "precio": 5.0, "unidades_vendidas": 0, "stock": 1, "genero_literario": "Varios", "apellido_autor": "N/A", "porcentaje_autor": 0.0, "estado_impresion": "activo", "categoria": "Ficción"},
        {"isbn": "978-7", "titulo": "Crónica de una Muerte Anunciada", "precio": 20.0, "unidades_vendidas": 800, "stock": 15, "genero_literario": "Ficción", "apellido_autor": "García Márquez", "porcentaje_autor": 0.15, "estado_impresion": "activo", "categoria": "Ficción"},
        {"isbn": "978-8", "titulo": "Introducción a la IA", "precio": 45.0, "unidades_vendidas": 300, "stock": 10, "genero_literario": "Programación", "apellido_autor": "Russell", "porcentaje_autor": 0.10, "estado_impresion": "activo", "categoria": "Académico"},
        {"isbn": "978-9", "titulo": "Don Quijote", "precio": 30.0, "unidades_vendidas": 400, "stock": 5, "genero_literario": "Ficción", "apellido_autor": "Cervantes", "porcentaje_autor": 0.10, "estado_impresion": "activo", "categoria": "Ficción"},
        {"isbn": "978-10", "titulo": "Anatomía Humana", "precio": 70.0, "unidades_vendidas": 100, "stock": 8, "genero_literario": "Medicina", "apellido_autor": "Netter", "porcentaje_autor": 0.15, "estado_impresion": "activo", "categoria": "Académico"}
    ]

    print("=" * 60)
    print("A. FASE DE LIMPIEZA E INDEXACIÓN")
    print("=" * 60)
    catalogo_activo, total_descartados = generar_catalogo_activo(lista_libros)
    print(f"[!] Libros descartados por reglas de negocio: {total_descartados}")
    print(f"[*] Registros procesados válidos: {len(catalogo_activo)}\n")
    
    print("=" * 60)
    print("B. FASE DE ANÁLISIS Y ORDENAMIENTO (Regalías Proyectadas)")
    print("=" * 60)
    libros_ordenados = calcular_regalias_pendientes(catalogo_activo)
    for lib in libros_ordenados:
        print(f" -> {lib['titulo']} | Autor: {lib['apellido_autor']} | Regalía Proyectada: ${lib['regalia_proyectada']:.2f}")
    
    print("\n" + "=" * 60)
    print("C. FASE DE ESTRUCTURACIÓN PARA INTERFAZ GRÁFICA")
    print("=" * 60)
    vista_final = estructurar_vista_generos(libros_ordenados)
    
    json_formateado = json.dumps(vista_final, indent=4, ensure_ascii=False)
    print(json_formateado)
    
    ruta_salida = "vista_libreria.json"
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(json_formateado)
    
    print("\n[*] Éxito: El JSON ha sido guardado físicamente en el archivo '{0}'".format(ruta_salida))
