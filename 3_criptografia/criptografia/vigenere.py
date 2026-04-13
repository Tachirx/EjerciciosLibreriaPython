def _procesar_vigenere(texto, palabra_clave, cifrar=True):
    """
    Implementación del cifrado Vigenère manipulando iteraciones de strings multiclave.
    
    Args:
        texto (str): Mensaje
        palabra_clave (str): Contraseña texto.
    """
    if not palabra_clave.isalpha():
        raise ValueError("Vigenère estricto requiere una palabra clave alfabética.")
        
    resultado = ""
    palabra_clave = palabra_clave.upper()
    clave_idx = 0
    longitud_clave = len(palabra_clave)
    
    for caracter in texto:
        if caracter.isalpha():
            base_ascii = ord('A') if caracter.isupper() else ord('a')
            
            # Extraemos el equivalente numérico de la letra actual de la clave
            letra_clave_actual = palabra_clave[clave_idx % longitud_clave]
            desplazamiento = ord(letra_clave_actual) - ord('A')
            
            if not cifrar:
                 desplazamiento = -desplazamiento
                 
            nuevo_ascii = (ord(caracter) - base_ascii + desplazamiento) % 26 + base_ascii
            resultado += chr(nuevo_ascii)
            
            # Incrementamos el índice para rotar el ciclo letreado de la palabra clave
            clave_idx += 1
        else:
            resultado += caracter
            
    return resultado

def cifrar_vigenere(texto, clave):
    return _procesar_vigenere(texto, clave, cifrar=True)

def descifrar_vigenere(texto, clave):
    return _procesar_vigenere(texto, clave, cifrar=False)
