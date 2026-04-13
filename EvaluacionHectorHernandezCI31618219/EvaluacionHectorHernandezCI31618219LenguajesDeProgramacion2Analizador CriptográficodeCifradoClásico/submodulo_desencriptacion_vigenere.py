def desencriptar_vigenere(): ##Submodulo para la desencriptacion de los mensajes utilizando el metodo Vigenere
    print("===Ha seleccionado la desencriptacion Vigenere===")
    msj_encriptado = input("\n\nDigite el mensaje a desencriptar: ")
    while True:
        clave = input("Digite la clave para la desencriptacion: ")
        if clave.isalpha():
            clave.upper()
            break
        else:
            print("\n\n===La clave solo debe contener letras, intentelo nuevamente===")
    msj_desencriptado = ""
    indice_clave = 0
    for letra in msj_encriptado:
        if letra.isalpha():
            pos_inicio = ord("a") if letra.lower() else ord("A")
            desplazamiento = ord(clave[indice_clave % len(clave)]) - ord("A")
            letra_ascii = ord(letra)
            pos_nueva = (letra_ascii - pos_inicio - desplazamiento) % 26 + pos_inicio
            msj_desencriptado += chr(pos_nueva)
            indice_clave += 1
        else:
            msj_desencriptado += letra
    return msj_desencriptado