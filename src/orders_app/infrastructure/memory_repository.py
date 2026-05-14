from orders_app.db.models import Order
from orders_app.domain.repositories import OrderRepository


class MemoryOrderRepository:
    def __init__(self):
        self._orders: dict[int, Order] = {}
        self._id = 1

    def save(self, order: Order) -> Order:
        order.id = self._id
        self._orders[self._id] = order
        self._id += 1
        return order

    def list(self) -> list[Order]:
        return list(self._orders.values())

    def add(self, order: Order) -> Order:
        order.id = self._id
        self._orders[self._id] = order
        self._id += 1
        return order

    def get(self, order_id: int):
        return self._orders.get(order_id)

    #def list(self):
     #   return list(self._orders.values())

    def delete(self, order: Order):
        self._orders.pop(order.id, None)       