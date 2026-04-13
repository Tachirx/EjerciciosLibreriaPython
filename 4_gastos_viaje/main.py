from calculos import generar_balance
from interfaz import formatear_recibo_general

def procesar_grupo(participantes):
    print("Iniciando procesamiento de grupo...")
    try:
        total, promedio, balances = generar_balance(participantes)
        formatear_recibo_general(total, promedio, balances)

    except ValueError as val_err:
        print(f"\n[ERROR DE REQUISITO DE DISEÑO]: {val_err}")

    except ZeroDivisionError:
        print("\n[ALERTA DE MATEMÁTICA PURA]: Intento de división por cero detectado en promedios.")
        print("La lista de participantes está vacía. Abortando cálculo.")

    except Exception as e_general:
        print(f"\n[ERROR SISTÉMICO]: Ocurrió un fallo no previsto: {e_general}")

if __name__ == "__main__":
    print("=== TEST 1: Grupo de 4 Amigos (Funcionamiento Normal) ===")
    grupo_normal = {
        "Andres": 200,
        "Maria": 50,
        "Julio": 100,
        "Sofia": 50
    }
    procesar_grupo(grupo_normal)

    print("=== TEST 2: Lista Vacía (Dispara ValueError) ===")
    grupo_vacio = {}
    procesar_grupo(grupo_vacio)

    from calculos import calcular_promedio
    print("\n=== TEST 3: Provocando el ZeroDivisionError de Sistema ===")
    try:
        res = sum([1, 2, 3]) / len([])
    except ZeroDivisionError as division_err:
        print(f"[RESCATE INTERNO] No puedes dividir {sum([1,2,3])} entre 0: {division_err}")
