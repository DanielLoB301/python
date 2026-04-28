import time

"""
Context Managers (with)
Son estructuras que permiten ejecutar código antes y después de un bloque automáticamente.

Sirven para:

Manejar recursos (archivos, conexiones)
Garantizar limpieza
Ejecutar lógica de inicio y cierre
Medir tiempo
Controlar errores
Aseguran que el “cierre” ocurra incluso si hay excepciones.
"""


class Temporizador:
    def __enter__(self):
        self.inicio = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        fin = time.time()
        print(f"Tiempo: {fin - self.inicio:.4f} segundos")


with Temporizador():
    sum(range(10_000_000))
