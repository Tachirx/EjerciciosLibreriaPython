class ProductoAgotadoError(Exception):
    def __init__(self, producto):
        self.mensaje = f"¡AGOTADO! El producto '{producto}' no tiene unidades disponibles."
        super().__init__(self.mensaje)

class SaldoInsuficienteError(Exception):
    def __init__(self, falta):
        self.mensaje = f"SALDO INSUFICIENTE: Te faltan ${falta} para completar la compra."
        super().__init__(self.mensaje)

class DenominacionInvalidaError(Exception):
    def __init__(self, monto):
        self.mensaje = f"ERROR DE PAGO: El monto ${monto} no es válido (debe ser mayor a 0)."
        super().__init__(self.mensaje)
