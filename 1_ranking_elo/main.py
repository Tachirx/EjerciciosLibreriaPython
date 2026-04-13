from procesador import procesar_lote_partidas
from datos import base_datos_jugadores

def mostrar_ranking_estado():
    """Muestra el estado actual de la tabla de clasificación en memoria."""
    print(f"{'Jugador':<15} | {'Elo Actual':<10} | {'Partidas'}")
    print("-" * 40)
    # Ordenamos el diccionario por Elo descendente para la visualización
    ranking = sorted(base_datos_jugadores.items(), key=lambda x: x[1]["elo"], reverse=True)
    for nombre, datos in ranking:
        print(f"{nombre:<15} | {datos['elo']:<10} | {datos['partidas_jugadas']}")
    print("-" * 40)

if __name__ == "__main__":
    print("Estado INICIAL de Jugadores:")
    mostrar_ranking_estado()
    
    lote_simulado = [
        "Carlos | Ana | 1",       # Carlos gana a Ana
        "Luis | Marta | 1/2",     # Empate
        "Pedro | Ana | 0",        # Error: Pedro no existe (Prueba JugadorNoEncontradoError)
        "Carlos | Luis",          # Error de formato (faltan campos)
        "Marta | Carlos | 0",     # Carlos gana a Marta
        "Juan_Invalido | 0 | XY"  # Multiples errores en linea corrupta
    ]
    
    procesar_lote_partidas(lote_simulado)
    
    print("Estado FINAL de Jugadores:")
    mostrar_ranking_estado()
