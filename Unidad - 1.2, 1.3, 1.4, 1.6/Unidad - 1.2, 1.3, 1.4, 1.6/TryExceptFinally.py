archivo = None # Inicializamos la variable fuera del try
try:
    archivo = open("mi_documento.txt", "w") # SI NO LO TIENE CREELO, SI QUIERE FORZAR EL FILENOTFOUND, PONGA UN NOMBRE DE ARCHIVO QUE NO EXISTA O UNA RUTA INCORRECTA
    archivo.write("Hola, Programación 2!")      
    # Forzamos un error para ver qué pasa
    resultado = 10 / 0

except FileNotFoundError:
    print("Error: El archivo o directorio no existe.")

except Exception as e: # 'Exception' es una clase base que atrapa casi cualquier error
    print(f"Ocurrió un error inesperado: {e}")

finally:
    print("Ejecutando el bloque finally.")
    if archivo:
        archivo.close()
        print("El archivo ha sido cerrado correctamente.")

# MAS EJEMPLOS (COMENTADOS)

'''
try:
    conexion = conectar_bd()
    resultado = conexion.ejecutar("SELECT * FROM usuarios")
except Exception as e:
    print("Error en la consulta:", e)
finally:
    conexion.cerrar()  # Se cierra la conexión pase lo que pase
'''

'''
try:
    print("Procesando datos...")
    procesar()
except Exception:
    print("Hubo un error.")
finally:
    print("Proceso terminado.")  # Siempre se muestra
'''