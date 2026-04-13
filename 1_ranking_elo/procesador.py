from core_elo import calcular_nuevo_elo
from datos import obtener_jugador, actualizar_elo_jugador, JugadorNoEncontradoError

def procesar_lote_partidas(lote_partidas):
    """
    Procesa una lista de partidas en formato string y actualiza la base de datos.
    
    Args:
        lote_partidas (list[str]): Lista de strings con formato "JugadorA | JugadorB | Resultado".
                                   Resultado puede ser 1 (Gana A), 0 (Gana B) o 1/2 (Empate).
    """
    print("\n--- Iniciando Procesamiento por Lotes (Torneo) ---")
    
    for indice, linea in enumerate(lote_partidas):
        try:
            # División de la línea basada en el separador
            partes = [p.strip() for p in linea.split("|")]
            
            # Validación de formato estricto
            if len(partes) != 3:
                raise ValueError(f"Formato incorrecto. Se esperaban 3 segmentos, se encontraron {len(partes)}.")
                
            jugador_a_nombre, jugador_b_nombre, resultado_str = partes
            
            # Mapeo del resultado a valor numérico
            if resultado_str == "1":
                resultado_a = 1.0
            elif resultado_str == "0":
                resultado_a = 0.0
            elif resultado_str == "1/2":
                resultado_a = 0.5
            else:
                raise ValueError(f"Resultado no válido: '{resultado_str}'. Debe ser 1, 0 o 1/2.")
                
            # Recuperamos los datos de los jugadores de la "Base de datos"
            # Esto puede lanzar JugadorNoEncontradoError
            jugador_a = obtener_jugador(jugador_a_nombre)
            jugador_b = obtener_jugador(jugador_b_nombre)
            
            # Cálculo del algoritmo estructurado
            nuevo_elo_a, nuevo_elo_b = calcular_nuevo_elo(
                elo_a=jugador_a["elo"],
                elo_b=jugador_b["elo"],
                resultado_a=resultado_a
            )
            
            # Guardamos los nuevos valores
            actualizar_elo_jugador(jugador_a_nombre, nuevo_elo_a)
            actualizar_elo_jugador(jugador_b_nombre, nuevo_elo_b)
            
            print(f"[OK] Partida {indice+1}: {jugador_a_nombre} vs {jugador_b_nombre} procesada correctamente.")
            
        except JugadorNoEncontradoError as error_jugador:
            print(f"[ERROR-JUGADOR] Línea {indice+1} ('{linea}'): {error_jugador}")
        except ValueError as error_valor:
            print(f"[ERROR-FORMATO] Línea {indice+1} ('{linea}'): {error_valor}. Saltando registro corrompido.")
        except Exception as error_general:
            # Atrapa cualquier otro error no previsto para no romper el bucle (Robustez del Staff Engineer)
            print(f"[ERROR-DESCONOCIDO] Línea {indice+1} ('{linea}'): {error_general}")
            
    print("--- Finalizó el Procesamiento del Lote ---\n")
