import Funciones

def menu():

    print("1: Numeoro mayor a 10")
    print("2: Suma igual al tercero")
    print("3: Dividir el cuadrado")
    print("4: Obtener Grados celcius")
    opc = int(input(" Ingrese la opcion deseada:"))

 if( opc == 1):
        Funciones.mayorA10()


    elif( opc == 2):
        primernum = int(input("Ingrese el primer número entero: "))
        segundonum = int(input("Ingrese el segundo número entero: "))
        tercernum = int(input("Ingrese el tercer número entero: "))
        Funciones.suma_tres_numeros(primernum, segundonum, tercernum)

    elif( opc == 3):
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        act3 = Funciones.division_de_cuadrados(num1, num2)
        return print(act3)

    elif ( opc == 4):
        act4 = funciones.que_temperatura_es_en_celcius()
        return print(act4)

menu()
