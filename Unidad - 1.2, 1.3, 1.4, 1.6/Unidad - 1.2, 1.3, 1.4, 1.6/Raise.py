def registrar_usuario(edad):
    """Registra un usuario si la edad es válida."""
    if edad < 0:
        # La edad negativa no es un error para Python, pero sí para nuestra lógica.
        # Por lo tanto, lanzamos una excepción para señalarlo.
        raise ValueError("La edad no puede ser un número negativo.")
    elif edad < 18:
        print("Usuario registrado, pero es menor de edad.")
    else:
        print("Usuario mayor de edad registrado correctamente.")

# --- Ahora usamos la función dentro de un bloque try ---
try:
    registrar_usuario(25)  # Funciona
    registrar_usuario(15)  # Funciona
    registrar_usuario(-5)  # Esto lanzará nuestro error

except ValueError as e:
    # Atrapamos la excepción que nosotros mismos lanzamos
    print(f"Error en el registro: {e}")

