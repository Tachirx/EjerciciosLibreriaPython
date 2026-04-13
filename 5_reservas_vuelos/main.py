from vuelos.reservas import procesar_reserva_vuelo
from vuelos.gestion import base_datos_vuelos

def print_estado_vuelos():
    """Observabilidad del sistema"""
    print("\n[ESTADO GLOBAL DE LA AEROLÍNEA]")
    for codigo, datos in base_datos_vuelos.items():
        ocupados = len(datos['asientos_ocupados'])
        espera = len(datos['lista_de_espera'])
        print(f"| {codigo} | Ocupación: {ocupados}/{datos['capacidad_total']} | En Espera: {espera} |")

def main():
    print("=== TEST 1: Reserva Normal Exitosa ===")
    pasajero_1 = {"id": "P-202", "nombre": "Ana Garcia"}
    procesar_reserva_vuelo("V-001", pasajero_1)
    
    # En este momento V-001 ya tiene a 'Carlos Perez' (Hardcoded en db) y a 'Ana Garcia'. (2/2) Capacidad Máxima Llenada.
    
    print("=== TEST 2: Overbooking Provocado (Lanza Excepción y mueve a Espera) ===")
    pasajero_2 = {"id": "P-303", "nombre": "Jose Lopez"}
    procesar_reserva_vuelo("V-001", pasajero_2)
    
    print("=== TEST 3: Vuelo Inexistente (No genera ticket, es error de ValueError temprano) ===")
    try:
        procesar_reserva_vuelo("V-XYZ", pasajero_2)
    except Exception as e:
        print(f"Atrapado error externo: {e}")
        
    print("=== TEST 4: Reserva Invalida (Formato ID Incorrecto) ===")
    pasajero_malo = {"id": "A-999", "nombre": "Troll"} # Debe empezar con P-
    procesar_reserva_vuelo("V-002", pasajero_malo)
    
    print_estado_vuelos()

if __name__ == "__main__":
    main()
