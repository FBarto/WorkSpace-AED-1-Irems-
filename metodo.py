
def ingreso():
    cuenta = input("Ingrese una cuenta")
    monto = int(input("Ingrese monto "))
    lista={cuenta:monto}
    return lista


def mostrar(lista):
    print(lista.values())

def montMay1000(lista):
    if lista.values