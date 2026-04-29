from fastapi import APIRouter
from typing import List
from ..schemas.order import OrderCreate, OrderOut

router = APIRouter(prefix="/orders", tags=["orders"])

fake_db = []


@router.post("/", response_model=OrderOut)
def create_order(order: OrderCreate):
    new_order = {
        "id": len(fake_db) + 1,
        "user_id": order.user_id,
        "total": order.total,
    }
    fake_db.append(new_order)
    return new_order


@router.get("/", response_model=List[OrderOut])
def list_orders():
    return fake_db