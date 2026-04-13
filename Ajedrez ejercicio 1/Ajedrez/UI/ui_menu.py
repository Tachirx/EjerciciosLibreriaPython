import os
from core.core_elo import SistemaRanking

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class InterfazUsuario:
    def __init__(self):
        self.sistema = SistemaRanking()

    def menu_principal(self):
        while True:
            limpiar_pantalla()
            print(" === SISTEMA ELO UNEFA (MODULAR) ===")
            print(" 1. Registrar Jugadores")
            print(" 2. Procesar Lote de Partidas")
            print(" 3. Ver Ranking")
            print(" 4. Salir")
            op = input("\n➤ Opción: ")

            if op == "1": self.registrar_ui()
            elif op == "2": self.lote_ui()
            elif op == "3": self.ranking_ui()
            elif op == "4": break

    def registrar_ui(self):
        nombre = input("Nombre: ").strip()
        pts = input("Elo (Enter para 1200): ")
        elo = int(pts) if pts.isdigit() else 1200
        if self.sistema.agregar_jugador(nombre, elo):
            print("¡Registrado!")
        else:
            print("Error: Ya existe.")
        input("Enter...")

    def lote_ui(self):
        print("Ingrese 'JugadorA | JugadorB | Resultado' (FIN para terminar):")
        while True:
            linea = input("➤ ")
            if linea.upper() == "FIN": break
            try:
                j1, j2, res = [p.strip() for p in linea.split("|")]
                exito, msg = self.sistema.procesar_partida(j1, j2, float(res))
                if not exito: print(f" Error: {msg}")
            except:
                print(" Formato inválido.")
        input("Proceso terminado. Enter...")

    def ranking_ui(self):
        limpiar_pantalla()
        ranking = self.sistema.obtener_ranking_ordenado()
        print(f"{'Pos':<4} {'Jugador':<15} | {'Elo':<6} | {'PJ':<4}")
        print("-" * 35)
        for i, (nom, s) in enumerate(ranking, 1):
            print(f"{i:<4} {nom:<15} | {s['elo']:<6} | {s['pj']:<4}")
        input("\nPresione Enter...")
