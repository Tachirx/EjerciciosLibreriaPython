from errores import ProductoAgotadoError 
my_inventario = {
    "A1": {"Producto": "Papitas", "Cantidad": 0, "Precio": 500},
    "B2": {"Producto": "Galletas", "Cantidad": 6, "Precio": 800},
    "C3": {"Producto": "Refresco", "Cantidad": 10, "Precio": 300},
    "D4": {"Producto": "Caramelo", "Cantidad": 0, "Precio": 300},
}

def consultar_producto(codigo):
    if codigo not in my_inventario:
        return None
    
    info = my_inventario[codigo]
    if info["Cantidad"] <= 0:
        raise ProductoAgotadoError(info["Producto"])
    return info

def reducir_stock(codigo):
    if my_inventario[codigo]["Cantidad"] > 0:
        my_inventario[codigo]["Cantidad"] -= 1
