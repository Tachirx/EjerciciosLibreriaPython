class ProductoAgotadoError(Exception):
    """Excepción lanzada cuando un producto seleccionado no tiene stock continuo."""
    pass

class SaldoInsuficienteError(Exception):
    """Excepción lanzada cuando el monto ingresado es menor al precio del producto."""
    pass

class DenominacionInvalidaError(Exception):
    """Excepción lanzada cuando el usuario ingresa una moneda o billete no aceptado."""
    pass

# Inventario estructurado en diccionarios anidados
catalogo_productos = {
    "A1": {"nombre": "Agua Mineral", "precio": 1.50, "cantidad": 5},
    "B2": {"nombre": "Refresco Cola", "precio": 2.25, "cantidad": 2},
    "C3": {"nombre": "Galletas de Chocolate", "precio": 1.80, "cantidad": 0}, # Agotado (Prueba exception)
    "D4": {"nombre": "Papas Fritas", "precio": 2.50, "cantidad": 10}
}

# Monedas disponibles inicialmente en la caja (Dólares/Euros genéricos)
caja_monedas = {
    0.25: 10,
    0.50: 10,
    1.00: 20,
    5.00: 5
}

def consultar_producto(codigo):
    """Consulta si un código es válido y devuelve el producto."""
    if codigo not in catalogo_productos:
        raise ValueError(f"El código '{codigo}' es completamente inválido en esta máquina.")
    
    producto = catalogo_productos[codigo]
    
    # Check específico y temprano para modularidad transaccional
    if producto["cantidad"] <= 0:
        raise ProductoAgotadoError(f"El producto '{producto['nombre']}' se ha agotado en stock interno.")
        
    return producto

def reducir_inventario(codigo):
    """Baja el stock de la máquina una vez dispensado válidamente."""
    catalogo_productos[codigo]["cantidad"] -= 1

def aceptar_denominacion(monto):
    """Verifica si la moneda de entrada pertenece al sistema legal."""
    denominaciones_validas = [0.25, 0.50, 1.00, 2.00, 5.00, 10.00]
    if monto not in denominaciones_validas:
        raise DenominacionInvalidaError(f"La denominación de ${monto} no es reconocida por el lector de billetes/monedas.")
    return True
