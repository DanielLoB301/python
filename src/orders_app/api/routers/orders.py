from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from orders_app.api.deps import get_db
from orders_app.db.models import Order
from orders_app.api.schemas.order import OrderCreate, OrderOut
from typing import List
from orders_app.api.auth import get_current_user
from orders_app.infrastructure.sql_repository import SqlOrderRepository
from orders_app.domain.services import OrderService

from fastapi import HTTPException
from orders_app.domain.pricing import NormalPricing

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    repo = SqlOrderRepository(db)
    service = OrderService(repo, NormalPricing())

    try:
        return service.create_order(order.user_id, order.total)
    except ValueError:
        raise HTTPException(status_code=400)


@router.get("/", response_model=List[OrderOut])
def list_orders(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Order).all()

@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order no encontrada")
    return order


@router.put("/{order_id}", response_model=OrderOut)
def update_order(order_id: int, data: OrderCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order no encontrada")

    order.user_id = data.user_id
    order.total = data.total

    db.commit()
    db.refresh(order)
    return order


@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order no encontrada")

    db.delete(order)
    db.commit()
    return {"detail": "Order eliminada"}    