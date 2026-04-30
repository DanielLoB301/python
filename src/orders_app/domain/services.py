from orders_app.db.models import Order
from orders_app.domain.pricing import PricingStrategy
from orders_app.domain.repositories import OrderRepository
from orders_app.infrastructure.cache_decorator import simple_cache


class OrderService:
    def __init__(self, repository: OrderRepository, pricing: PricingStrategy):
        self.repository = repository
        self.pricing = pricing

    def create_order(self, user_id: int, total: float) -> Order:
        total = self.pricing.calculate(total)

        if total > 10000:
            raise ValueError("Total excede límite permitido")

        order = Order(user_id=user_id, total=total)
        return self.repository.add(order)


    @simple_cache
    def list_orders(self):
        return self.repository.list()