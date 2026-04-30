from typing import Protocol, List
from orders_app.db.models import Order


class OrderRepository(Protocol):
    def add(self, order: Order) -> Order:
        ...

    def get(self, order_id: int) -> Order | None:
        ...

    def list(self) -> List[Order]:
        ...

    def delete(self, order: Order) -> None:
        ...