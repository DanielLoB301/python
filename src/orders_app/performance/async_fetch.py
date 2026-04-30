import asyncio
import httpx
import time

URL = "https://jsonplaceholder.typicode.com/posts/1"

async def fetch(client):
    response = await client.get(URL)
    return response.json()

async def main():
    inicio = time.time()

    async with httpx.AsyncClient() as client:
        tareas = [fetch(client) for _ in range(10)]
        await asyncio.gather(*tareas)

    fin = time.time()
    print("Tiempo async:", fin - inicio)

if __name__ == "__main__":
    asyncio.run(main())