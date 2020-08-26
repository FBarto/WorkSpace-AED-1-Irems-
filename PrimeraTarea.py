def mayorDe10(num):

    if (num >10):
        print(f"El Numero {num} Es mayor a 10")
    else:
        print(f"El Numero {num} Es Menor o igual a 10")

"""------------------------------------------------------------------------------------------------"""

def divCuadrado(num1,num2):
    may=0
    men=0
    if(num1==num2):
        print(f"Los numero son iguales")
        elif (num1>num2):
        may= num1
        men= num2
    else:
        may=num2
        men=num1

    div = (may * may)/(men*men)
    print(f"Su resultado es: {div}")


"""----------------------------------------------------------------------------------------------"""
def celcius(f):

    c=(5/9)*(f-32)
    print(f"La temperatura expresada en grados celcius es {c}°")

"""----------------------------------------------------------------------------------------------"""
def numero():
    Num = int(input("Ingrese un numero"))
        if(Num>0):
            print(f"El numero es positivo")
        elif(Num<0):
            print(f"El numero es negativo")
        else:
            print(f"Su numero es 0")
""""--------------------------------------------------------------------------------------------"""
def esIgual(num1, num2, num3):
    if( (num1 + num2) == num3):
        print(f'La suma de {num1} y {num2} es igual a {num3}')
    else:
        print(f'La suma de {num1} y {num2} es distinta a {num3}')


"""     
1) Escribir un algoritmo que lea un número entero y verifique si es mayor a 10. Si lo es
escribir el número y si no lo es escribir un mensaje que diga que el número es menor o
igual.


2) Dados dos número enteros, se necesita saber el resultado de dividir el cuadrado del
mayor de ellos y el cuadrado del menor de ellos. Si los números son iguales escribir un
mensaje.


3) Escribir un algoritmo que convierta temperaturas de Fahrenheit a Celcius. Utilizar la
fórmula ºC = (5/9)·(ºF – 32).


4) Determinar si un número ingresado es: negativo, cero o positivo e imprimir, de
acuerdo a cada caso, el mensaje correspondiente.


5) Dados 3 números, determinar si la suma del primero y el segundo es igual al tercero.
Si se cumple, escribir &quot;La suma es igual al tercero&quot;, si no, escribir &quot;La suma es distinta
al tercero"""