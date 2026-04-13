### Estructuras Básicas

## Ejercicio 1 - Gestor de Invitados (Listas e If):
'''Crea una lista con tres nombres de invitados. 
   Pide al usuario que ingrese un nombre. Si el nombre está en la lista, elimínalo (fingiendo que ya entró). 
   Si no está, añádelo al final usando .append(). Imprime la lista final.'''

invitados_evento = ["Ana", "Carlos", "Beatriz"]
nombre_ingresado = input("Ingrese el nombre del invitado: ")

if nombre_ingresado in invitados_evento:
    invitados_evento.remove(nombre_ingresado)
    print(f"El invitado {nombre_ingresado} ya ingresó. Eliminando de la lista...")
else:
    invitados_evento.append(nombre_ingresado)
    print(f"El invitado {nombre_ingresado} no estaba en la lista. Añadiendo...")

print(f"Lista final de invitados: {invitados_evento}\n")


## Ejercicio 2 - Desempaquetando Datos (Tuplas):
'''Crea una tupla que contenga tres datos de un producto: (nombre, precio, cantidad). 
   Desempaqueta esos valores en tres variables distintas y usa un print formateado (f-string) para mostrar 
   un mensaje como: "Tenemos [cantidad] unidades de [nombre] a $[precio] cada una".'''

datos_producto = ("Laptop", 1250.00, 15)
nombre_articulo, precio_articulo, cantidad_articulo = datos_producto
print(f"Tenemos {cantidad_articulo} unidades de {nombre_articulo} a ${precio_articulo} cada una.\n")


## Ejercicio 3 - Limpieza de Base de Datos (Sets):
'''Tienes una lista de correos electrónicos donde algunos están repetidos: 
   ["a@a.com", "b@b.com", "a@a.com", "c@c.com"]. Conviértela en un Set para eliminar los duplicados, 
   y luego devuélvela a formato Lista. Imprime el resultado.'''

correos_base_datos = ["a@a.com", "b@b.com", "a@a.com", "c@c.com"]
correos_limpios = list(set(correos_base_datos))
print(f"Correos filtrados y sin duplicados: {correos_limpios}\n")


### Bucles y Control de Flujo

## Ejercicio 4 - El Cajero Automático (While y Break):
'''Crea un bucle while True que le pida al usuario una contraseña. Si el usuario escribe "secreto123", 
   imprime "Acceso concedido" y rompe el bucle con break. Si escribe cualquier otra cosa, 
   imprime "Contraseña incorrecta, intente de nuevo"'''

while True:
    contrasena_usuario = input("Ingrese la contraseña del cajero: ")
    if contrasena_usuario == "secreto123":
        print("Acceso concedido\n")
        break
    else:
        print("Contraseña incorrecta, intente de nuevo")


## Ejercicio 5 - Inventario Bajo (Diccionarios y For):
'''Crea un diccionario con 4 productos y sus cantidades en stock 
   (ej. {"manzanas": 10, "peras": 3, "uvas": 20}). Usa un bucle for con .items() 
   para recorrerlo e imprimir solo los productos que tengan menos de 5 unidades.'''

inventario_almacen = {"manzanas": 10, "peras": 3, "uvas": 20, "kiwis": 2}
print("Alerta de stock bajo para los siguientes productos:")
for nombre_producto, cantidad_stock in inventario_almacen.items():
    if cantidad_stock < 5:
        print(f"- {nombre_producto}: solo quedan {cantidad_stock} unidades")
print()


## Ejercicio 6 - Saltando los Impares (For, Range y Continue):
'''Usa un bucle for y range() para iterar del 1 al 15. Si el número es impar, 
   usa continue para saltarlo. Si es par, imprímelo en pantalla.'''

print("Imprimiendo números pares del 1 al 15:")
for numero_actual in range(1, 16):
    if numero_actual % 2 != 0:
        continue
    print(numero_actual)
print()


### Match / Case (Emparejamiento de patrones estructurales)

## Ejercicio 7 - El Botón Inteligente (Match y Wildcard):
'''Escribe un programa que evalúe una variable de texto llamada accion. 
   Usa match para que si es "encender", imprima "Sistema ON"; si es "apagar", 
   imprima "Sistema OFF". Usa el wildcard _ para que cualquier otra palabra imprima "Comando no reconocido".'''

accion_sistema = input("Ingrese una acción para el sistema (encender/apagar): ").strip().lower()
match accion_sistema:
    case "encender":
        print("Sistema ON")
    case "apagar":
        print("Sistema OFF")
    case _:
        print("Comando no reconocido")