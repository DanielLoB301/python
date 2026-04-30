import httpx
import time

URL = "https://jsonplaceholder.typicode.com/posts/1"

def fetch():
    with httpx.Client() as client:
        return client.get(URL).json()

def main():
    inicio = time.time()

    for _ in range(10):
        fetch()

    fin = time.time()
    print("Tiempo sync:", fin - inicio)

if __name__ == "__main__":
    main()