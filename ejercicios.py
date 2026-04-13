import secrets
import string

def generar_contrasena(longitud: int = 12, incluir_simbolos: bool = True) -> str:
    """
    Genera una contraseña aleatoria segura.
    
    Args:
        longitud (int): La longitud de la contraseña. Por defecto es 12.
        incluir_simbolos (bool): Si es True, incluye símbolos especiales.
        
    Returns:
        str: La contraseña generada.
    """
    # LETRAS MAYUSCULAS, MINUSCULAS Y NUMEROS
    caracteres = string.ascii_letters + string.digits
    
    # SIMBOLOS
    if incluir_simbolos:
        caracteres += string.punctuation
        
    # GENERACIÓN DE LA CONTRASEÑA
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    
    return contrasena

if __name__ == "__main__":
    # LO QUE ESPERO QUE PASE:
    print("Contraseña estándar (12 caracteres con símbolos):")
    print(generar_contrasena())
    
    print("\nContraseña más larga (16 caracteres con símbolos):")
    print(generar_contrasena(longitud=16))
    
    print("\nContraseña PIN numérico/alfabético (8 caracteres sin símbolos):")
    print(generar_contrasena(longitud=8, incluir_simbolos=False))
