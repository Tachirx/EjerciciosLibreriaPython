# ==========================================
# ESTRUCTURAS DE CONTROL: IF, ELIF, ELSE
# ==========================================

# 1. ESTRUCTURA BÁSICA (If / Else)
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# 2. MÚLTIPLES CONDICIONES (Elif)
# 'elif' es la abreviatura de 'else if'. Se usa para evaluar varias opciones.
nota = 85

if nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C")
else:
    print("Calificación: F (Reprobado)")


# 3. OPERADORES LÓGICOS (and, or, not)
# Puedes combinar varias condiciones en un solo 'if'
tiene_entrada = True
tiene_dinero = False

if tiene_entrada or tiene_dinero:
    print("Puedes pasar al concierto.")

hambre = True
comida_lista = False

if hambre and not comida_lista:
    print("Toca cocinar algo.")


# 4. IF EN UNA SOLA LÍNEA (Operador Ternario)
# Muy útil para asignaciones rápidas de variables
puntuacion = 10
resultado = "Ganaste" if puntuacion >= 10 else "Perdiste"
print(f"Resultado del juego: {resultado}")


# 5. EVALUACIÓN DIRECTA (Truthy / Falsy)
# No necesitas hacer 'if lista == []', Python lo entiende solo
carrito = []

if not carrito:
    print("El carrito está vacío, ¡ve a comprar algo!")


# 6. CONDICIONALES ANIDADOS
# Un 'if' dentro de otro 'if' (úsalos con moderación para no enredarte)
usuario_activo = True
es_admin = True

if usuario_activo:
    if es_admin:
        print("Bienvenido al panel de control.")
    else:
        print("Bienvenido, usuario estándar.")
else:
    print("Cuenta suspendida.")