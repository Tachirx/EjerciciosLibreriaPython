class JugadorNoEncontradoError(Exception):
    """Excepción lanzada cuando un jugador no existe en la base de datos simulada."""
    pass

# Simulamos una base de datos en memoria (Diccionario)
base_datos_jugadores = {
    "Carlos": {"elo": 1500, "partidas_jugadas": 10},
    "Ana": {"elo": 1600, "partidas_jugadas": 15},
    "Luis": {"elo": 1450, "partidas_jugadas": 8},
    "Marta": {"elo": 1550, "partidas_jugadas": 12}
}

def obtener_jugador(nombre):
    """
    Busca un jugador en la base de datos.
    
    Args:
        nombre (str): Nombre del jugador a buscar.
        
    Returns:
        dict: Registro del jugador.
        
    Raises:
        JugadorNoEncontradoError: Si el jugador no existe.
    """
    if nombre not in base_datos_jugadores:
        raise JugadorNoEncontradoError(f"El jugador '{nombre}' no se encuentra registrado en el sistema.")
    return base_datos_jugadores[nombre]

def actualizar_elo_jugador(nombre, nuevo_elo):
    """
    Actualiza el Elo y las partidas jugadas de un jugador.
    
    Args:
        nombre (str): Nombre del jugador.
        nuevo_elo (float): Nuevo puntaje Elo a registrar.
    """
    jugador = obtener_jugador(nombre)
    jugador["elo"] = nuevo_elo
    jugador["partidas_jugadas"] += 1
