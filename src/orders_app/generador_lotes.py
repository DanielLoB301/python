"""
Son funciones que producen valores uno por uno usando yield, en lugar de devolver todo de una vez.

Permiten:

Ahorrar memoria
Procesar grandes volúmenes de datos
Trabajar de manera eficiente y pausada
Se ejecutan de forma “perezosa” (lazy evaluation).
"""


def generar_lotes(lista, tamaño):
    for i in range(0, len(lista), tamaño):
        yield lista[i : i + tamaño]


for lote in generar_lotes([1, 2, 3, 4, 5, 6], 2):
    print(lote)
