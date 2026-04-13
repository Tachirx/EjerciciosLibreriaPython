def encriptacion_cesar(): #Submodulo para encriptar mensajes con el metodo cesar
    print("===Ha seleccionado la encriptacion cesar===\n")
    msj_sin_encriptar = input("Digite el mensaje a encriptar: ")
    while True:
        try:
            clave_numerica = int(input("Digite un numero entero del 1 al 26 que servira como clave numerica: "))
            break
        except ValueError:
            print("\n\nLa clave numerica debe ser un numero entero\n intenta de nuevo")
    msj_encriptado = ""
    for letra in msj_sin_encriptar:
        if letra.isalpha() == True:
            inicio_pos = ord("a") if letra.islower() else ord("A")
            letra_ascii = ord(letra)
            nueva_pos = (letra_ascii - inicio_pos + clave_numerica) % 26 + inicio_pos
            msj_encriptado += chr(nueva_pos)
        else:
            msj_encriptado += letra
    return msj_encriptado