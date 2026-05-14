from orders_app.application.use_cases import CreateOrderUseCase
from orders_app.infrastructure.memory_repository import MemoryOrderRepository
from orders_app.domain.notification_port import NotificationPort


class FakeNotifier(NotificationPort):
    def __init__(self):
        self.messages = []

    def notify(self, message: str):
        self.messages.append(message)


def test_create_order_use_case():
    repo = MemoryOrderRepository()
    notifier = FakeNotifier()

    use_case = CreateOrderUseCase(repo, notifier)

    order = use_case.execute(user_id=1, total=100)

    assert order.id == 1
    assert order.total == 100
    assert len(notifier.messages) == 1