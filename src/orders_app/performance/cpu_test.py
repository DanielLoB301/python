from concurrent.futures import ProcessPoolExecutor
import time

def trabajo_pesado(n):
    total = 0
    for i in range(10_000_000):
        total += i * n
    return total

def main():
    inicio = time.time()

    with ProcessPoolExecutor() as executor:
        list(executor.map(trabajo_pesado, range(4)))

    fin = time.time()
    print("Tiempo multiprocessing:", fin - inicio)

if __name__ == "__main__":
    main()