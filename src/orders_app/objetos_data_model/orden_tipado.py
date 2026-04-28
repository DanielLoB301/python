from dataclasses import dataclass
from typing import List


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


class Order:
    def __init__(self) -> None:
        self.items: List[OrderItem] = []

    def agregar_item(self, item: OrderItem) -> None:
        self.items.append(item)

    def total(self) -> float:
        return sum(item.subtotal() for item in self.items)


if __name__ == "__main__":
    p1 = Producto("Laptop", 1000.0)
    p2 = Producto("Mouse", 50.0)

    item1 = OrderItem(p1, 1)
    item2 = OrderItem(p2, 2)

    orden = Order()
    orden.agregar_item(item1)
    orden.agregar_item(item2)

    print("Total:", orden.total())
