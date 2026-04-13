'''
3. Analizador Criptográfico de Cifrado Clásico
Crea una suite de herramientas de consola para cifrar y descifrar mensajes utilizando 
métodos clásicos (César y Vigenère), demostrando el dominio sobre el tipo de dato string 
y sus métodos.

Requerimientos:

	Lógica: Manipulación de cadenas a bajo nivel usando iteraciones (for/while), conversión 
    de caracteres a sus valores ASCII (ord(), chr()) y aritmética modular. No se permite 
    importar módulos de criptografía.

	Paquetes: Construye un paquete criptografia que contenga un submódulo para cada 
    algoritmo y un módulo principal de enrutamiento.

	Manejo de Errores: Valida estrictamente las entradas. Si el usuario ingresa una 
    clave alfabética cuando se espera una numérica (César), el programa debe atrapar 
    el ValueError nativo, transformarlo en un mensaje amigable y volver a pedir el dato 
    sin romper la ejecución (bucle de reintento).
'''

print("\n===Analizador criptografico de cifrado clasico===\n\n1) Digite ´cesar´ para el metodo Cesar\n2) Digite ´vigenere´ para el metodo Vigenere\n3) Digite ´salir´ para terminar el programa")
opcion = input("\nSeleccione el metodo de encriptado para trabajar: ")
match opcion.lower():
    case "cesar":
        print("\n===Ha seleccionado el metodo Cesar===\n1) Digite ´encriptar´ para encriptar un mensaje\n2) Digite ´desencriptar´ para desencriptar un mensaje\n3) Presione cualquier tecla y presione enter para salir")
        operacion = input("\nDigite la operacion que desea realizar: ")
        match operacion.lower():
            case "encriptar":
                from criptografia.submodulo_encriptacion_cesar import encriptacion_cesar
                print(f"\n\nEl mensaje encriptado es: {encriptacion_cesar()}")
                print("\n===Fin del programa, hasta la proxima===")
            case "desencriptar":
                from criptografia.submodulo_desencriptacion_cesar import desencriptacion_cesar
                print(f"\n\nEl mensaje desencriptado es: {desencriptacion_cesar()}")
                print("\n===Fin del programa, hasta la proxima===")
            case _:
                print("\n==No a seleccionado ninguna operacion==")
    case "vigenere":
        print("\n===Ha seleccionado el metodo Vigenere===\n\n1) Digite ´encriptar´ para encriptar un mensaje\n2) Digite ´desencriptar´ para desencriptar un mensaje\n3) Presione cualquier tecla y presione enter para salir")
        operacion = input("\nDigite la operacion que desea realizar: ")
        match operacion.lower():
            case "encriptar":
                from criptografia.submodulo_encriptacion_vigenere import encriptar_vigenere
                print(f"\n\nEl mensaje encriptado es: {encriptar_vigenere()}")
                print("Fin del programa, hasta la proxima")
            case "desencriptar":
                from criptografia.submodulo_desencriptacion_vigenere import desencriptar_vigenere
                print(f"\n\nEl mensaje desencriptado es: {desencriptar_vigenere()}")
                print("Fin del programa, hasta la proxima")
            case _:
                print("\n==No a seleccionado ninguna operacion==")
    case "salir":
        print("\n\n====Fin del programa, hasta la proxima====\n\n")