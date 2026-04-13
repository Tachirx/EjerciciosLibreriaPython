# Importamos solo las funciones sumar y restar
from operaciones import sumar, restar

# Ahora podemos usarlas directamente sin el prefijo
resultado_suma = sumar(15, 7)
resultado_resta = restar(15, 7)

print(f"La suma es: {resultado_suma}")
print(f"La resta es: {resultado_resta}")

# Ojo: la variable PI no fue importada, por lo que esto daría un error:
# print(PI) # NameError: name 'PI' is not defined