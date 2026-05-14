from orders_app.domain.entities import Order
from orders_app.domain.repositories import OrderRepository
from orders_app.domain.notification_port import NotificationPort


class CreateOrderUseCase:
    def __init__(
        self,
        repository: OrderRepository,
        notifier: NotificationPort,
    ):
        self.repository = repository
        self.notifier = notifier

    def execute(self, user_id: int, total: float) -> Order:
        if total > 10000:
            raise ValueError("Total excede límite permitido")

        order = Order(id=None, user_id=user_id, total=total)

        saved = self.repository.save(order)

        self.notifier.notify(f"Order creada: {saved.id}")

        return saved