import math
import os

class JugadorNoEncontradoError(Exception):
    pass

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_elo(r_a, r_b, resultado, k=32):
    # Cálculo de probabilidad esperada
    exp_a = 1 / (1 + 10 ** ((r_b - r_a) / 400))
    exp_b = 1 - exp_a
    
    # Nuevos puntajes
    nuevo_a = round(r_a + k * (resultado - exp_a))
    nuevo_b = round(r_b + k * ((1 - resultado) - exp_b))
    
    return max(0, nuevo_a), max(0, nuevo_b)

class SistemaRankingAvanzado:
    def __init__(self):
        self.jugadores = {}

    def inscribir_jugadores_lote(self):
        while True:
            limpiar_pantalla()
            print("=== REGISTRO DE NUEVOS JUGADORES ===")
            nombre = input("\n➤ Nombre del jugador (o Enter para volver): ").strip()
            
            if not nombre:
                break
            if nombre in self.jugadores:
                print(f" ¡Error! '{nombre}' ya existe.")
                input("Presione Enter...")
                continue

            while True:
                pts_in = input(f"➤ Puntos Elo iniciales para {nombre} (Enter para 1200): ").strip()
                if pts_in == "":
                    puntos = 1200
                    break
                try:
                    puntos = int(pts_in)
                    break
                except ValueError:
                    print(" Error: Ingrese un número entero.")

            self.jugadores[nombre] = {
                "elo": puntos,
                "pj": 0,
                "g": 0,
                "p": 0,
                "e": 0
            }
            print(f" {nombre} registrado correctamente.")
            if input("\n¿Inscribir a otro? (s/n): ").lower() != 's':
                break

    def registrar_partida(self):
        if len(self.jugadores) < 2:
            limpiar_pantalla()
            print(" Se requieren al menos 2 jugadores registrados.")
            input("\nPresione Enter...")
            return

        while True:
            limpiar_pantalla()
            print("=== REGISTRAR RESULTADO ===")
            print(f"Jugadores disponibles: {', '.join(self.jugadores.keys())}")
            
            j1 = input("\n➤ Jugador A (Blanco): ").strip()
            j2 = input("➤ Jugador B (Negro): ").strip()

            if j1 not in self.jugadores or j2 not in self.jugadores:
                print(" Error: Uno o ambos jugadores no existen.")
                input(); continue
            if j1 == j2:
                print(" Error: Un jugador no puede jugar contra sí mismo.")
                input(); continue
            break

        while True:
            print(f"\n{j1}({self.jugadores[j1]['elo']}) vs {j2}({self.jugadores[j2]['elo']})")
            res_in = input("Resultado (1: Gana A, 0: Gana B, 0.5: Empate): ").strip()
            if res_in in ['1', '0', '0.5']:
                resultado = float(res_in)
                break
            print(" Resultado inválido.")

        n_a, n_b = calcular_elo(self.jugadores[j1]['elo'], self.jugadores[j2]['elo'], resultado)
        
        # Actualizar Stats
        self.jugadores[j1]['elo'] = n_a
        self.jugadores[j2]['elo'] = n_b
        self.jugadores[j1]['pj'] += 1
        self.jugadores[j2]['pj'] += 1

        if resultado == 1:
            self.jugadores[j1]['g'] += 1
            self.jugadores[j2]['p'] += 1
        elif resultado == 0:
            self.jugadores[j2]['g'] += 1
            self.jugadores[j1]['p'] += 1
        else:
            self.jugadores[j1]['e'] += 1
            self.jugadores[j2]['e'] += 1

        print(f"\n ¡Duelo finalizado! {j1}: {n_a} pts | {j2}: {n_b} pts")
        input("\nPresione Enter...")

    def ver_ranking(self):
        limpiar_pantalla()
        print(f"{'RANKING DETALLADO':^65}")
        print("=" * 65)
        print(f"{'Pos':<4} {'Jugador':<15} | {'Elo':<6} | {'PJ':<4} | {'G':<3} | {'P':<3} | {'E':<3}")
        print("-" * 65)
        
        if not self.jugadores:
            print(f"{'No hay registros':^65}")
        else:
            ranking = sorted(self.jugadores.items(), key=lambda x: x[1]['elo'], reverse=True)
            for i, (nom, stats) in enumerate(ranking, 1):
                print(f"{i:<4} {nom:<15} | {stats['elo']:<6} | {stats['pj']:<4} | "
                      f"{stats['g']:<3} | {stats['p']:<3} | {stats['e']:<3}")
        
        print("=" * 65)
        input("\nPresione Enter para volver...")

    def menu(self):
        while True:
            limpiar_pantalla()
            print(" ============================================")
            print(" ║      Motor de Elo Ajedrez UNEFA        ║")
            print(" ============================================")
            print(" 1. Inscribir Jugadores ")
            print(" 2. Registrar Partida")
            print(" 3. Ver Ranking y Stats")
            print(" 4. Salir")
            opcion = input("\n➤ Opción: ")

            if opcion == "1":
                self.inscribir_jugadores_lote()
            elif opcion == "2":
                self.registrar_partida()
            elif opcion == "3":
                self.ver_ranking()
            elif opcion == "4":
                print("¡Hasta luego!")
                break

if __name__ == "__main__":
    app = SistemaRankingAvanzado()
    app.menu()