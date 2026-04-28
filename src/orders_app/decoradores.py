import functools
import random
import time

"""Decoradores
Son funciones que modifican o amplían el comportamiento de otra función sin cambiar su código interno.

Sirven para agregar funcionalidades como:

Validación
Logging
Reintentos
Control de acceso
Medición de tiempo
Permiten aplicar lógica reutilizable alrededor de funciones.
"""


def reintentos(max_intentos=3, delay=1):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            intentos = 0
            while intentos < max_intentos:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    intentos += 1
                    print(f"Error: {e}. Reintentando...")
                    time.sleep(delay * intentos)
            raise Exception("Máximo de intentos alcanzado")

        return wrapper

    return decorador


@reintentos(max_intentos=3)
def funcion_inestable():
    if random.random() < 0.7:
        raise ValueError("Falló algo")
    print("Funcionó correctamente")


funcion_inestable()
