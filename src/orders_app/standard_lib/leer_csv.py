from pathlib import Path
import csv


def leer_ventas() -> None:
    archivo = Path(__file__).resolve().parent.parent / "data" / "ventas.csv"

    if not archivo.exists():
        print("Archivo no encontrado")
        return

    with archivo.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        total_general = 0.0

        for fila in reader:
            producto = fila["producto"]
            precio = float(fila["precio"])
            cantidad = int(fila["cantidad"])

            total = precio * cantidad
            total_general += total

            print(f"{producto}: {total}")

        print(f"\nTotal general: {total_general}")


if __name__ == "__main__":
    leer_ventas()