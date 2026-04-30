from sqlalchemy import String, Integer,ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column,relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email})"
    
class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    total: Mapped[float] = mapped_column(Float)

    user = relationship("User", back_populates="orders")


User.orders = relationship("Order", back_populates="user")