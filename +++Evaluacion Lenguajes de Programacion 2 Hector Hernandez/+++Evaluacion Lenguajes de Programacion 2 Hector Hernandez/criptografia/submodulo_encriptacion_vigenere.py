def encriptar_vigenere(): ##Submodulo para la encriptacion de los mensajes utilizando el metodo Vigenere
    print("===Ha seleccionado la encriptacion Vigenere===") 
    msj_a_encriptar = input("\n\nDigite el mensaje a encriptar: ") 
    while True: 
        clave = input("\nDigite una clave para la encriptacion: ")
        if clave.isalpha(): 
            clave = clave.upper() 
            break 
        else:
            print("===La clave solo debe contener letras, intentelo nuevamente===")
    msj_encriptado = ""
    indice_clave = 0
    for letra in msj_a_encriptar:
        if letra.isalpha():
            pos_inicio = ord("a") if letra.lower() else ord("A")
            desplazamiento = ord(clave[indice_clave % len(clave)]) - ord("A")
            letra_ascii = ord(letra.upper())
            pos_nueva = (letra_ascii - ord("A") + desplazamiento) % 26
            msj_encriptado += chr(pos_nueva+pos_inicio)
            indice_clave += 1
        else:
            msj_encriptado += letra
    return msj_encriptado