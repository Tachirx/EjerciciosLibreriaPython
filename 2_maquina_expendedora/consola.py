from transacciones import procesar_compra
from inventario import catalogo_productos

def mostrar_vitrina():
    """Genera una interfaz interactiva simulada en terminal."""
    print("\n" + "="*40)
    print("      MÁQUINA EXPENDEDORA v2026")
    print("="*40)
    for codigo, data in catalogo_productos.items():
        estado = f"Disponibles: {data['cantidad']}" if data['cantidad'] > 0 else "--- AGOTADO ---"
        print(f"[{codigo}] {data['nombre']:<22} | ${data['precio']:.2f} | {estado}")
    print("="*40)

def main():
    mostrar_vitrina()
    
    # Simulación Casos de Uso del Motor de Estados
    print("\n--- TEST 1: Compra Exitosa Exacta ---")
    procesar_compra("A1", [1.0, 0.50]) # Cuesta 1.50
    
    print("\n--- TEST 2: Compra Exitosa con Vuelto ---")
    procesar_compra("B2", [1.0, 1.0, 1.0]) # Cuesta 2.25, paga 3
    
    print("\n--- TEST 3: Producto Agotado (Lanza ProductoAgotadoError) ---")
    procesar_compra("C3", [2.0]) # C3 empieza en 0
    
    print("\n--- TEST 4: Saldo Insuficiente (Lanza SaldoInsuficienteError) ---")
    procesar_compra("D4", [1.0]) # Cuesta 2.50, paga 1
    
    print("\n--- TEST 5: Moneda No Reconocida (Lanza DenominacionInvalidaError) ---")
    procesar_compra("A1", [0.45, 1.0]) 

if __name__ == "__main__":
    main()
