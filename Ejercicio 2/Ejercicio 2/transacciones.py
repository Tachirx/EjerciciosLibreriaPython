from errores import SaldoInsuficienteError, DenominacionInvalidaError
def validar_pago(precio_producto, pago_usuario):
    if pago_usuario <= 0:
        raise DenominacionInvalidaError(pago_usuario)
    
    if pago_usuario < precio_producto:
        falta = precio_producto - pago_usuario
        raise SaldoInsuficienteError(falta)
    return pago_usuario - precio_producto
