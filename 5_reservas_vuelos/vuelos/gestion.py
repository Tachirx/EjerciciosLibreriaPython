# Base de Datos Simulada (Diccionario Maestro en Memoria)
base_datos_vuelos = {
    "V-001": {
        "origen": "Madrid",
        "destino": "Buenos Aires",
        "capacidad_total": 2, # Capacidad ultra-baja para forzar overbooking rápido en pruebas
        "asientos_ocupados": [
            {"id": "P-100", "nombre": "Carlos Perez"}
        ],
        "lista_de_espera": []
    },
    "V-002": {
        "origen": "Tokio",
        "destino": "Nueva York",
        "capacidad_total": 5,
        "asientos_ocupados": [],
        "lista_de_espera": []
    }
}

def consultar_vuelo(codigo_vuelo):
    """Retorna el diccionario interno del vuelo si existe."""
    if codigo_vuelo not in base_datos_vuelos:
        raise ValueError(f"El vuelo {codigo_vuelo} no existe en el sistema de la aerolínea.")
    return base_datos_vuelos[codigo_vuelo]

def verificar_disponibilidad(codigo_vuelo):
    """Verifica si quedan asientos libres mediante conteo de memoria."""
    vuelo = consultar_vuelo(codigo_vuelo)
    ocupados = len(vuelo["asientos_ocupados"])
    total = vuelo["capacidad_total"]
    
    return ocupados < total, (total - ocupados)
