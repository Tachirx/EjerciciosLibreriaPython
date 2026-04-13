def sumar_total(participantes_pagos):
    return sum(participantes_pagos.values())

def calcular_promedio(total, cantidad_participantes):
    if cantidad_participantes == 0:
        raise ValueError("No hay participantes")
    return total / cantidad_participantes

def generar_balance(participantes_pagos):
    cantidad = len(participantes_pagos)
    total_general = sumar_total(participantes_pagos)
    cuota_justa = calcular_promedio(total_general, cantidad)

    balances = {}
    for nombre, pagado in participantes_pagos.items():
        balances[nombre] = round(pagado - cuota_justa, 2)

    return total_general, cuota_justa, balances
