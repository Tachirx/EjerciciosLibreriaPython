"""
Módulo principal: Motor de Cálculo Elo.
Contiene la fórmula matemática pura estructurada.
"""

def calcular_nuevo_elo(elo_a, elo_b, resultado_a, factor_k=32):
    """
    Calcula el nuevo Elo para dos jugadores tras una partida.
    
    Args:
        elo_a (float): Elo actual del jugador A.
        elo_b (float): Elo actual del jugador B.
        resultado_a (float): Resultado desde la perspectiva de A (1 victoria, 0 derrota, 0.5 empate).
        factor_k (int): Factor de desarrollo (constante de ajuste).
        
    Returns:
        tuple[float, float]: Nuevos puntajes (nuevo_elo_a, nuevo_elo_b).
    """
    # Esperanza de victoria para cada jugador (Probabilidad)
    esperanza_a = 1 / (1 + 10 ** ((elo_b - elo_a) / 400))
    esperanza_b = 1 / (1 + 10 ** ((elo_a - elo_b) / 400))
    
    # Resultado para B es el complemento del resultado de A
    resultado_b = 1 - resultado_a
    
    # Cálculo del nuevo Elo
    nuevo_elo_a = elo_a + factor_k * (resultado_a - esperanza_a)
    nuevo_elo_b = elo_b + factor_k * (resultado_b - esperanza_b)
    
    return round(nuevo_elo_a, 2), round(nuevo_elo_b, 2)
