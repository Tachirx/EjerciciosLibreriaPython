import inventario
import transacciones
from errores import ProductoAgotadoError, SaldoInsuficienteError, DenominacionInvalidaError

def ejecutar_maquina():
    print("--- BIENVENIDO A LA EXPENDEDORA ---")
    codigo = input("Ingrese el código del producto (A1, B2, C3, D4): ").upper()
    
    pago_realizado = 0.0
    compra_exitosa = False 
    
    try:
        prod_info = inventario.consultar_producto(codigo)
        if not prod_info:
            print("Código inválido.")
            return

        print(f"Elegiste {prod_info['Producto']}. Precio: ${prod_info['Precio']}")
    
        entrada_pago = input("Ingrese su pago: ")
        pago_realizado = float(entrada_pago)
        
        vuelto = transacciones.validar_pago(prod_info['Precio'], pago_realizado)
        inventario.reducir_stock(codigo)
        print(f"Dispensando {prod_info['Producto']}...")
        print(f"Compra exitosa. Su vuelto es: ${vuelto}")
        compra_exitosa = True 

    except (ProductoAgotadoError, SaldoInsuficienteError, DenominacionInvalidaError) as e:
        print(f"TRANSACCIÓN FALLIDA: {e}")
    except ValueError:
        print("Error: Ingrese un número válido para el pago.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    finally:
        
        if not compra_exitosa and pago_realizado > 0:
            print(f"SISTEMA: Reembolsando ${pago_realizado} íntegros al usuario.")
        elif compra_exitosa:
            print("SISTEMA: Transacción finalizada correctamente.")

if __name__ == "__main__":
    ejecutar_maquina()
