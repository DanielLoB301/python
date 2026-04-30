from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from orders_app.api.deps import get_db
from orders_app.db.models import Order
from orders_app.api.schemas.order import OrderCreate, OrderOut
from typing import List
from orders_app.api.auth import get_current_user


router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = Order(user_id=order.user_id, total=order.total)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


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