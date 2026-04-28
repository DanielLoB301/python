from pathlib import Path
import csv
import json
import logging
from datetime import datetime
from typing import List, Dict


# -----------------------
# Configuración de logging
# -----------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# -----------------------
# Rutas
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CSV_FILE = DATA_DIR / "ventas.csv"
JSON_FILE = DATA_DIR / "resultado.json"


# -----------------------
# Funciones
# -----------------------
def leer_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        logging.error("El archivo CSV no existe.")
        return []

    logging.info("Leyendo archivo CSV...")

    with path.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def calcular_metricas(datos: List[Dict[str, str]]) -> Dict:
    total_general = 0.0
    total_items = 0

    for fila in datos:
        try:
            precio = float(fila["precio"])
            cantidad = int(fila["cantidad"])
        except (ValueError, KeyError) as e:
            logging.warning(f"Fila inválida detectada: {fila} - {e}")
            continue

        total_general += precio * cantidad
        total_items += cantidad

    resultado = {
        "timestamp": datetime.utcnow().isoformat(),
        "total_general": total_general,
        "total_items_vendidos": total_items,
        "numero_registros": len(datos),
    }

    logging.info("Métricas calculadas correctamente.")
    return resultado


def exportar_json(path: Path, datos: Dict) -> None:
    logging.info("Exportando resultados a JSON...")

    with path.open(mode="w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

    logging.info(f"Archivo JSON generado en: {path}")


def main() -> None:
    logging.info("Iniciando procesamiento de ventas...")

    datos = leer_csv(CSV_FILE)

    if not datos:
        logging.error("No hay datos para procesar.")
        return

    metricas = calcular_metricas(datos)
    exportar_json(JSON_FILE, metricas)

    logging.info("Proceso finalizado correctamente.")


if __name__ == "__main__":
    main()