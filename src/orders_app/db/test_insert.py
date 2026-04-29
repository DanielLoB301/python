from .database import SessionLocal
from .models import User


def insertar_usuario() -> None:
    db = SessionLocal()

    nuevo_usuario = User(name="Juan", email="juan@example.com")

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    print("Usuario insertado:", nuevo_usuario)

    db.close()


if __name__ == "__main__":
    insertar_usuario()