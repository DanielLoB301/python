class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def precio_con_impuesto(self, impuesto: float = 0.16) -> float:
        return self.precio * (1 + impuesto)


if __name__ == "__main__":
    p1 = Producto("Laptop", 1000)
    p2 = Producto("Mouse", 50)

    print(p1.precio_con_impuesto())
    print(p2.precio_con_impuesto())
