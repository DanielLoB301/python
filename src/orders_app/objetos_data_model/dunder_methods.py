class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def precio_con_impuesto(self, impuesto: float = 0.16) -> float:
        return self.precio * (1 + impuesto)

    def __str__(self):
        return f"Producto(nombre={self.nombre}, precio={self.precio})"

    def __eq__(self, other):
        if not isinstance(other, Producto):
            return False
        return self.nombre == other.nombre


if __name__ == "__main__":
    p1 = Producto("Laptop", 1000)
    p2 = Producto("Laptop", 1200)

    print(p1)
    print(p1 == p2)
