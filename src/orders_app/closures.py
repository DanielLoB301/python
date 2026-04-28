# Un closure es:
# Una función dentro de otra
# Que recuerda variables de la función externa
# Aunque la función externa ya terminó


def crear_multiplicador(numero):
    def multiplicar(x):
        return x * numero

    return multiplicar


por_dos = crear_multiplicador(2)
print(por_dos.__closure__[0].cell_contents)
print(por_dos(5))
