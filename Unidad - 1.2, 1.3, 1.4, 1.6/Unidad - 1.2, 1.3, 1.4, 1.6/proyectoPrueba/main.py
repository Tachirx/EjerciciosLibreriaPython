# Importar el módulo 'operaciones' del sub-paquete 'basicas'
from matematicas.basicas import operaciones

# Importar una función específica del módulo 'trigonometria'
from matematicas.avanzadas.trigonometria import seno

# Usamos la función del módulo 'operaciones'
suma = operaciones.sumar(20, 10)
print(f"Suma desde el paquete: {suma}")

# Usamos la función importada directamente
resultado_seno = seno(90) # Suponiendo que la función 'seno' existe en trigonometria
print(f"Seno de 90: {resultado_seno}")