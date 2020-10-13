import Funciones1
Bandera =1
if (Bandera == 1):
    print("1: Numero mayor a 10")
    print("2: Suma igual al tercero")
    print("3: Dividir el cuadrado")
    print("4: Obtener Grados celcius")
    print("0: Para salir del programa")
    opc = int(input(" Ingrese la opcion deseada:"))
if (opc == 1):
    Funciones1.mayorA10()
elif (opc == 2):
    a = int(input("ingrese primer numero"))
    b = int(input("ingrese segundo numero"))
    c = int(input("ingrese tercer numero"))

    Funciones1.tresNum(a,b,c)

elif (opc == 3):
    d = int(input("Ingrese un numero"))
    f = int(input("Ingrese un numero"))

    Funciones1.dosNum()
elif (opc == 4):
    Funciones1.celcius()
    print()
else: (Bandera == 0)