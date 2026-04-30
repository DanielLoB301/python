from orders_app.db.models import Order
from orders_app.domain.repositories import OrderRepository


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, user_id: int, total: float) -> Order:
        if total > 10000:
            raise ValueError("Total excede límite permitido")

        order = Order(user_id=user_id, total=total)
        return self.repository.add(order)

    def list_orders(self):
        return self.repository.list()