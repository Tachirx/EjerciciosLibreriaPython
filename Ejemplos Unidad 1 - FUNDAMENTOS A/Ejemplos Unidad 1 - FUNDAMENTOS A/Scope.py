# ==========================================
# REGLA LEGB: PRIORIDAD DE SCOPE EN PYTHON
# ==========================================

# 1. [B]uilt-in (Integradas)
# Son las funciones que ya vienen con Python, como len(), print(), etc.
from math import pi # 'pi' es un ejemplo de algo que ya existe

# 2. [G]lobal (Globales)
# Variables definidas en el cuerpo principal del archivo (.py)
nombre = "Global"

def funcion_externa():
    # 3. [E]nclosing (Envolventes)
    # Variables en una función que contiene a otra función (anidadas)
    nombre = "Enclosing"
    
    def funcion_interna():
        # 4. [L]ocal (Locales)
        # Variables definidas dentro de la propia función actual
        nombre = "Local"
        
        print(f"Buscando 'nombre': {nombre}") # Resultado: Local

    funcion_interna()

# Ejecutamos para ver el orden
funcion_externa()


# --- ¿CÓMO FUNCIONA EL ORDEN? ---

variable_ejemplo = "ESTOY EN GLOBAL"

def demostrar_busqueda():
    # Si comento la línea de abajo, Python subirá al nivel Global
    # variable_ejemplo = "ESTOY EN LOCAL" 
    print(f"Valor encontrado: {variable_ejemplo}")

demostrar_busqueda()