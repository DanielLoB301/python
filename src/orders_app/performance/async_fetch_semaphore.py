import asyncio
import httpx
import time

URL = "https://jsonplaceholder.typicode.com/posts/1"
CONCURRENCIA_MAXIMA = 3


async def fetch(client, sem):
    async with sem:
        response = await client.get(URL)
        return response.json()


async def main():
    inicio = time.time()

    sem = asyncio.Semaphore(CONCURRENCIA_MAXIMA)

    async with httpx.AsyncClient() as client:
        tareas = [fetch(client, sem) for _ in range(10)]
        await asyncio.gather(*tareas)

    fin = time.time()
    print(f"Tiempo async con límite {CONCURRENCIA_MAXIMA}: {fin - inicio}")


if __name__ == "__main__":
    asyncio.run(main())