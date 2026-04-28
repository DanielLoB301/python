import json


def cargar_datos(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print("Archivo no encontrado")
    except json.JSONDecodeError:
        print("Formato JSON inválido")


def filtrar_por_cliente(datos, cliente):
    return [orden for orden in datos if orden["cliente"] == cliente]


def calcular_total(datos):
    return sum(orden["total"] for orden in datos)


def main():
    datos = cargar_datos("src/orders_app/orders.json")

    if not datos:
        return

    ordenes_ana = filtrar_por_cliente(datos, "Ana")
    total = calcular_total(ordenes_ana)

    print("Órdenes de Ana:", ordenes_ana)
    print("Total:", total)


if __name__ == "__main__":
    main()
