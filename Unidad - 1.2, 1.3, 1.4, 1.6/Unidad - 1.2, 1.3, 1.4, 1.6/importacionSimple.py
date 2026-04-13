# Importamos el módulo completo
import operaciones

# Para usar sus funciones, usamos la sintaxis: modulo.funcion()
resultado_suma = operaciones.sumar(10, 5)
resultado_resta = operaciones.restar(10, 5)

print(f"La suma es: {resultado_suma}")
print(f"La resta es: {resultado_resta}")

# También podemos acceder a las variables del módulo
print(f"El valor de PI es: {operaciones.PI}")