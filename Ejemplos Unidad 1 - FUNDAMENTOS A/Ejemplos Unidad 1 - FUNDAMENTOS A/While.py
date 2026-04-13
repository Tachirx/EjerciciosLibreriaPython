# ==========================================
# EL BUCLE WHILE EN PYTHON
# ==========================================

# 1. ESTRUCTURA BÁSICA
# Se repite mientras la condición se cumpla
contador = 1

print("--- Cuenta regresiva ---")
while contador <= 5:
    print(f"Número: {contador}")
    contador += 1  # IMPORTANTE: Si no sumas, el bucle será infinito


# 2. BUCLE CON BREAK (Cerrar por la fuerza)
# Útil para salir del bucle en un momento específico
print("\n--- Buscando el número 7 ---")
n = 1
while n < 20:
    if n == 7:
        print("¡Encontrado! Saliendo del bucle...")
        break  # Rompe el bucle de golpe
    n += 1


# 3. BUCLE CON CONTINUE (Saltar un paso)
# Salta el resto del código y vuelve al inicio del while para la siguiente vuelta
print("\n--- Imprimiendo solo impares ---")
x = 0
while x < 6:
    x += 1
    if x % 2 == 0:
        continue  # Si es par, salta el print y vuelve arriba
    print(f"Impar encontrado: {x}")


# 4. WHILE TRUE (Bucle "infinito" controlado)
# Muy común para menús o juegos que esperan una acción del usuario
print("\n--- Simulador de Menú ---")
while True:
    opcion = "salir" # Simulamos que el usuario escribió algo
    
    if opcion == "salir":
        print("Cerrando programa...")
        break # La única forma de salir de un While True es con break


# 5. EL PELIGRO: Bucle Infinito
# Si olvidas actualizar la variable de la condición, 
# el programa se quedará pegado gastando procesador.
# Ejemplo (¡No ejecutar!):
# while True:
#     print("No me detendré jamás")