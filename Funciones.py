
def mayorA10():
    n1= input(int("Ingrese un numero"))
    if ( n1 > 10 ):
        print(n1)
    else:
        print(f"{n1} Es menor a 10")

def sumaIgualTercero(a=0,b=0,c=0):
    suma = int(a + b)
    if(suma == c ):
        print(f"Las suma de {a} + {b}. Es igual a {c}")
    else:
        print(f"Las suma de {a} + {b}. No es igual a {c}")


def divCuadrado(nu1=1,nu2=1):
    may = 0
    men = 0
    if(nu1 == nu2):

        return nu1

    elif(nu1 > nu2):

        may = nu1
        men = nu2
    else:
        may = nu2
        men = nu1

    div = int((may*may)/(men*men))
    return div

def celcius():
    f =int(input("Ingrese la temp en grados fahrenheit."))
    c = int((5/9)*(f-32))
    return c