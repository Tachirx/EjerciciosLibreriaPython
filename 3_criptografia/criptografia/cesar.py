def _procesar_texto(texto, clave, cifrar=True):
    """
    Motor matemático modular para el cifrado César procesando iteración pura.
    
    Args:
        texto (str): Mensaje normal o encriptado a iterar.
        clave (int): Numeral de base para saltos ASCII.
        cifrar (bool): Sumamos la clave para cifrar, o restamos para volver al origen.
    """
    resultado = ""
    desplazamiento = clave if cifrar else -clave
    
    for caracter in texto:
        if caracter.isalpha():
            # Aritmética modular (Staff Engineer standard): Encontrar el offset real.
            base_ascii = ord('A') if caracter.isupper() else ord('a')
            
            # 1. Normalizamos (llevamos del 65 al 0 - en A-Z, o similar)
            # 2. Sumamos desplazamiento, y dividimos por 26 para que dé "la vuelta"
            # 3. Restauramos sumando base_ascii de vuelta (+65)
            
            nuevo_ascii = (ord(caracter) - base_ascii + desplazamiento) % 26 + base_ascii
            resultado += chr(nuevo_ascii)
        else:
            # Los espacios y signos de puntuación se dejan tal cual
            resultado += caracter
            
    return resultado

def cifrar_cesar(texto, clave):
    return _procesar_texto(texto, clave, cifrar=True)

def descifrar_cesar(texto, clave):
    return _procesar_texto(texto, clave, cifrar=False)
