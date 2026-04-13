# Importamos el módulo 'utilidades' de nuestro paquete 'mi_biblioteca'
from mi_biblioteca import utilidades

# Usamos las funciones
print(utilidades.saludar("Estudiante"))

numero_a_verificar = 10
if utilidades.es_par(numero_a_verificar):
    print(f"El número {numero_a_verificar} es par.")
else:
    print(f"El número {numero_a_verificar} es impar.")