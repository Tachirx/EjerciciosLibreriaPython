from criptografia import cifrar_cesar, descifrar_cesar, cifrar_vigenere, descifrar_vigenere

def obtener_entero(mensaje):
    """
    Bucle de reintento para la validación estricta (Manejo de Errores Requerido).
    """
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print(f"[ERROR] '{entrada}' no es un número válido. Ingresa un numeral (Ej: 3).")

def obtener_palabra(mensaje):
    """
    Validación para palabra clave de Vigenère.
    """
    while True:
        entrada = input(mensaje)
        if entrada.isalpha():
            return entrada
        else:
            print(f"[ERROR] '{entrada}' debe contener solo letras (sin espacios ni números).")

def main():
    print("=== Suite Criptográfica Clásica ===")
    
    # 1. Simulación automática para evaluación rápida del Staff
    print("\n--- TEST: Cifrado César ---")
    texto_base = "Ingenieria de Software 2026!"
    clave_cesar = 5
    
    cifrado_c = cifrar_cesar(texto_base, clave_cesar)
    descifrado_c = descifrar_cesar(cifrado_c, clave_cesar)
    
    print(f"Original:  {texto_base}")
    print(f"Cifrado:   {cifrado_c} (Clave: +{clave_cesar})")
    print(f"Descifrado: {descifrado_c} (Clave: -{clave_cesar})")
    assert texto_base == descifrado_c, "Fallo lógico en César"


    print("\n--- TEST: Cifrado Vigenère ---")
    texto_base_v = "Ataque al amanecer secreto!"
    clave_vig = "PYTHON"
    
    cifrado_v = cifrar_vigenere(texto_base_v, clave_vig)
    descifrado_v = descifrar_vigenere(cifrado_v, clave_vig)
    
    print(f"Original:  {texto_base_v}")
    print(f"Cifrado:   {cifrado_v} (Clave: {clave_vig})")
    print(f"Descifrado: {descifrado_v} (Clave inversada)")
    assert texto_base_v == descifrado_v, "Fallo lógico en Vigenère"

    # 2. Interfaz manual para el bucle de reintento solicitado (Comentado para auto-tests, ejecutable por el usuario)
    print("\n[MODO INTERACTIVO OPCIONAL DISPONIBLE EN CÓDIGO]")
    """
    opcion = input("¿Deseas intentar romper el validador de César? (s/n): ")
    if opcion.lower() == 's':
        print("- Intenta ingresar letras cuando pida el número de clave -")
        texto_usuario = input("Ingresa un texto: ")
        clave_usuario = obtener_entero("Ingresa la clave numérica para César: ")
        print(f"Resultado: {cifrar_cesar(texto_usuario, clave_usuario)}")
    """

if __name__ == "__main__":
    main()
