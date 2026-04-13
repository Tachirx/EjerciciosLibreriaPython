def formatear_recibo_general(total, promedio, balances):
    print("\n" + "="*50)
    print(f"       REPORTE FINANCIERO GRUPO DE VIAJE")
    print("="*50)
    print(f" Gasto Total del Viaje:           ${total:.2f}")
    print(f" Cuota Equitativa por Persona:    ${promedio:.2f}")
    print("-" * 50)

    for persona, saldo in balances.items():
        if saldo > 0:
            print(f" [{persona:<10}] A FAVOR : Recibe  ${saldo:>6.2f}")
        elif saldo < 0:
            print(f" [{persona:<10}] EN DEUDA: Pagar   ${abs(saldo):>6.2f}")
        else:
            print(f" [{persona:<10}] AL DÍA  : Saldo    $0.00")

    print("="*50 + "\n")
