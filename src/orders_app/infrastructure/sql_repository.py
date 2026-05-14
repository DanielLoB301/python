from sqlalchemy.orm import Session
from orders_app.domain.entities import Order
from orders_app.domain.repositories import OrderRepository
from orders_app.db.models import Order as ORMOrder


class SqlOrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, order: Order) -> Order:
        orm = ORMOrder(user_id=order.user_id, total=order.total)
        self.db.add(orm)
        self.db.commit()
        self.db.refresh(orm)
        return Order(id=orm.id, user_id=orm.user_id, total=orm.total)

    def list(self):
        rows = self.db.query(ORMOrder).all()
        return [
            Order(id=r.id, user_id=r.user_id, total=r.total)
            for r in rows
        ]