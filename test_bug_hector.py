mensaje = "Hola Mundo"
clave = "key"

print("=" * 50)
print(f"Mensaje original: '{mensaje}'")
print(f"Clave ingresada:  '{clave}'")
print("=" * 50)

clave.upper()
print(f"\nDespues de clave.upper(): '{clave}'  <-- Sigue en minusculas")

msj_hector = ""
indice_clave = 0
for letra in mensaje:
    if letra.isalpha():
        pos_inicio = ord("a") if letra.lower() else ord("A")
        desplazamiento = ord(clave[indice_clave % len(clave)]) - ord("A")
        letra_ascii = ord(letra)
        pos_nueva = (letra_ascii - pos_inicio + desplazamiento) % 26 + pos_inicio
        msj_hector += chr(pos_nueva)
        indice_clave += 1
    else:
        msj_hector += letra

clave_ok = clave.upper()
msj_correcto = ""
indice_clave = 0
for letra in mensaje:
    if letra.isalpha():
        pos_inicio = ord("a") if letra.islower() else ord("A")
        desplazamiento = ord(clave_ok[indice_clave % len(clave_ok)]) - ord("A")
        letra_ascii = ord(letra)
        pos_nueva = (letra_ascii - pos_inicio + desplazamiento) % 26 + pos_inicio
        msj_correcto += chr(pos_nueva)
        indice_clave += 1
    else:
        msj_correcto += letra

print(f"\nResultado Hector:   '{msj_hector}'  <-- Corrupto")
print(f"resultado correcto: '{msj_correcto}'  <-- Asi deberia salir")
