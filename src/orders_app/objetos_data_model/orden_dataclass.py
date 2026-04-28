from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    precio: float


@dataclass
class OrderItem:
    producto: Producto
    cantidad: int

    def subtotal(self) -> float:
        return self.producto.precio * self.cantidad


if __name__ == "__main__":
    p = Producto("Laptop", 1000)
    item = OrderItem(p, 2)

    print(item)
    print(item.subtotal())
