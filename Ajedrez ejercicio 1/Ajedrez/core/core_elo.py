import math

def calcular_elo(r_a, r_b, resultado, k=32):
    exp_a = 1 / (1 + 10 ** ((r_b - r_a) / 400))
    exp_b = 1 - exp_a
    
    nuevo_a = round(r_a + k * (float(resultado) - exp_a))
    nuevo_b = round(r_b + k * ((1 - float(resultado)) - exp_b))
    
    return max(0, nuevo_a), max(0, nuevo_b)

class SistemaRanking:
    def __init__(self):
        self.jugadores = {}

    def agregar_jugador(self, nombre, elo_inicial=1200):
        if nombre in self.jugadores:
            return False
        self.jugadores[nombre] = {
            "elo": elo_inicial, "pj": 0, "g": 0, "p": 0, "e": 0
        }
        return True

    def procesar_partida(self, j1, j2, resultado):
        if j1 not in self.jugadores or j2 not in self.jugadores:
            return False, "Uno de los jugadores no existe."
        
        n_a, n_b = calcular_elo(self.jugadores[j1]['elo'], self.jugadores[j2]['elo'], resultado)
        
        # Actualización de estadísticas
        self.jugadores[j1]['elo'], self.jugadores[j2]['elo'] = n_a, n_b
        self.jugadores[j1]['pj'] += 1
        self.jugadores[j2]['pj'] += 1

        if resultado == 1:
            self.jugadores[j1]['g'] += 1; self.jugadores[j2]['p'] += 1
        elif resultado == 0:
            self.jugadores[j2]['g'] += 1; self.jugadores[j1]['p'] += 1
        else:
            self.jugadores[j1]['e'] += 1; self.jugadores[j2]['e'] += 1
        
        return True, (n_a, n_b)

    def obtener_ranking_ordenado(self):
        return sorted(self.jugadores.items(), key=lambda x: x[1]['elo'], reverse=True)
