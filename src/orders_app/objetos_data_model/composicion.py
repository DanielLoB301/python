class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio


class OrderItem:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self) -> float:
        return self.producto.precio * self.cantidad


class Order:
    def __init__(self):
        self.items = []

    def agregar_item(self, item: OrderItem):
        self.items.append(item)

    def total(self) -> float:
        return sum(item.subtotal() for item in self.items)


if __name__ == "__main__":
    p1 = Producto("Laptop", 1000)
    p2 = Producto("Mouse", 50)

    item1 = OrderItem(p1, 1)
    item2 = OrderItem(p2, 2)

    orden = Order()
    orden.agregar_item(item1)
    orden.agregar_item(item2)

    print("Total:", orden.total())
