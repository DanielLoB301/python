from pydantic import BaseModel, Field


class OrderItemIn(BaseModel):
    nombre: str
    precio: float = Field(gt=0)
    cantidad: int = Field(gt=0)


if __name__ == "__main__":
    item = OrderItemIn(nombre="Laptop", precio=1000, cantidad=2)
    print(item)

    # Prueba error
    try:
        OrderItemIn(nombre="Laptop", precio=-10, cantidad=0)
    except Exception as e:
        print("Error de validación:")
        print(e)
