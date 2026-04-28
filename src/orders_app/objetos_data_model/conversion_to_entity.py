from dataclasses import dataclass

from pydantic import BaseModel, Field


@dataclass
class Producto:
    nombre: str
    precio: float


class ProductoIn(BaseModel):
    nombre: str
    precio: float = Field(gt=0)

    def to_entity(self) -> Producto:
        return Producto(nombre=self.nombre, precio=self.precio)


if __name__ == "__main__":
    entrada = ProductoIn(nombre="Laptop", precio=1000)
    entidad = entrada.to_entity()

    print(entrada)
    print(entidad)
    print(entidad.nombre)
    print(entidad.precio)
