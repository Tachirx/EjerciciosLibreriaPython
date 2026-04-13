from .excepciones import OverbookingError, ReservaInvalidaError
from .gestion import consultar_vuelo, verificar_disponibilidad
import random

def procesar_reserva_vuelo(codigo_vuelo, pasajero):
    """
    Motor del Overbooking. Intenta meter a alguien al vuelo, o a lista de espera.
    Genera transacciones garantizadas en finally.
    
    Args:
        codigo_vuelo (str): ID Vuelo.
        pasajero (dict): {"id": string, "nombre": string}
        
    Returns:
        tuple[bool, str]: Estado booleano de éxito de abordar general, mensaje.
    """
    estado_transaccion = "FALLIDA" # Default pessimista
    vuelo = consultar_vuelo(codigo_vuelo) # Falla temprana (ValueError) si no existe 
    
    try:
        # Validación de Integridad (Excepción Crítica 2)
        if "id" not in pasajero or "nombre" not in pasajero or not str(pasajero["id"]).startswith("P-"):
            raise ReservaInvalidaError(f"Datos del pasajero corruptos o IDs {pasajero.get('id')} no permitidos (Requiere P-XX).")
            
        print(f"\n>> Solicitud recibida: {pasajero['nombre']} para {codigo_vuelo}")
        
        # Validación de Capacidad Competitiva
        hay_espacio, libres = verificar_disponibilidad(codigo_vuelo)
        
        if not hay_espacio:
            # Excepción Crítica 1 (Lanzada y atrapada en el mismo flujo maestro)
            raise OverbookingError("Overbooking detectado. Vuelo a máxima capacidad comercial.")
            
        # Asignación Exitoso
        vuelo["asientos_ocupados"].append(pasajero)
        estado_transaccion = "EXITOSA"
        return True, "Pasajero abordado."
        
    except OverbookingError as over_err:
        print(f"[RECHAZO COMERCIAL] {over_err}")
        print("-- Acción Recomendada Automática: Moviendo a Lista de Espera...")
        vuelo["lista_de_espera"].append(pasajero)
        estado_transaccion = "EN ESPERA"
        return False, "En Lista de Espera."
        
    except ReservaInvalidaError as inv_err:
        print(f"[RECHAZO SISTEMA] {inv_err}")
        estado_transaccion = "FALLIDA"
        return False, "Error de Datos."
        
    finally:
        # Requisito Técnico Estricto: Always Execute (Ticket)
        codigo_tkt = f"TKT-{random.randint(1000, 9999)}"
        print("\n" + "*"*35)
        print(f"* TICKET DE TRANSACCIÓN: {codigo_tkt} *")
        print(f"* ESTADO: {estado_transaccion:<21} *")
        print("*"*35 + "\n")
