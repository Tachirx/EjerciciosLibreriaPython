def desencriptacion_cesar(): #Submodulo para desencriptar de mensajes con el metodo cesar
    print("===Ha seleccionado la desencriptacion cesar===\n")
    msj_encriptado = input("\nDigite el mensaje a desencriptar: ")
    while True:
        try:
            clave_numerica = int(input("Digite un numero entero del 1 al 26 que servira como clave numerica: "))
            break
        except ValueError:
            print("\n\nLa clave numerica debe ser un numero entero\n intenta de nuevo")
    msj_desencriptar = ""
    for letra in msj_encriptado:
        if letra.isalpha() == True:
            inicio_pos = ord("a") if letra.islower() else ord("A")
            letra_ascii = ord(letra)
            nueva_pos=(letra_ascii - inicio_pos - clave_numerica) % 26 + inicio_pos
            msj_desencriptar += chr(nueva_pos)
        else:
            msj_desencriptar += letra
    return msj_desencriptar