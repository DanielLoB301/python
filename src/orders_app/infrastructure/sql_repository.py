from sqlalchemy.orm import Session
from orders_app.db.models import Order
from orders_app.domain.repositories import OrderRepository


class SqlOrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, order: Order) -> Order:
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def get(self, order_id: int) -> Order | None:
        return self.db.get(Order, order_id)

    def list(self):
        return self.db.query(Order).all()

    def delete(self, order: Order):
        self.db.delete(order)
        self.db.commit()