import httpx
import time
import logging
from pathlib import Path
from typing import Any, Dict


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class HttpClient:
    def __init__(self, timeout: float = 5.0, max_reintentos: int = 3) -> None:
        self.timeout = timeout
        self.max_reintentos = max_reintentos

    def get_json(self, url: str) -> Dict[str, Any]:
        for intento in range(self.max_reintentos):
            try:
                logging.info(f"Intento {intento + 1} para {url}")

                with httpx.Client(timeout=self.timeout) as client:
                    response = client.get(url, follow_redirects=True)
                    response.raise_for_status()
                    return response.json()

            except httpx.RequestError as e:
                logging.warning(f"Error de red: {e}")

            except httpx.HTTPStatusError as e:
                logging.error(f"Error HTTP {e.response.status_code}")
                raise

            if intento == self.max_reintentos - 1:
                logging.error("Se alcanzó el máximo de intentos.")
                raise

            tiempo_espera = 2 ** intento
            logging.info(f"Reintentando en {tiempo_espera} segundos...")
            time.sleep(tiempo_espera)

        raise RuntimeError("Error inesperado")

    def descargar_archivo(self, url: str, destino: Path) -> None:
        logging.info(f"Descargando archivo desde {url}")

        destino.parent.mkdir(parents=True, exist_ok=True)

        try:
            with httpx.Client(timeout=self.timeout) as client:
                with client.stream("GET", url, follow_redirects=True) as response:
                    response.raise_for_status()

                    with destino.open("wb") as f:
                        for chunk in response.iter_bytes():
                            f.write(chunk)

            logging.info(f"Archivo guardado en {destino}")

        except httpx.RequestError as e:
            logging.error(f"Error de red: {e}")
            raise

        except httpx.HTTPStatusError as e:
            logging.error(f"Error HTTP {e.response.status_code}")
            raise


# --------------------------
# Ejecución directa
# --------------------------
if __name__ == "__main__":
    cliente = HttpClient(timeout=5.0, max_reintentos=3)

    # 1️⃣ Consumir API JSON
    data = cliente.get_json(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    print("Respuesta JSON:", data)

    # 2️⃣ Descargar archivo grande por streaming
    archivo_destino = Path("descargas/imagen.jpg")
    cliente.descargar_archivo(
        "https://picsum.photos/300",
        archivo_destino,
    )