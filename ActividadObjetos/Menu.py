from ActividadObjetos import Principal

def menu():
    lista = []
    opc = 1

    while (opc != 0):
        print(" 1- Crear nuevo ingreso de auto")
        print(" 2- Mostrar listado de autos")
        print(" 3- Salir")
        opc = int(input("Ingrese una opcion a a ejecutar: \n"))

        if (opc == 1):

            marca = input("Ingrese la marca del vehiculo:\n")
            modelo = input("Ingrese la modelo del vehiculo:\n")
            año = input("Ingrese el año del vehiculo:\n")
            precio_por_kilometro = int(input("Ingrese precio por kilometros:\n"))
            seguro_alquiler = int(input("Ingrese el costo del seguro a contratar:\n"))
            dni_cliente = input("Ingrese dni del cliente:\n")
            nombre_del_arrendatario = input("Ingrese nombre del cliemte:\n")
            kilmetros_recorridos = int(input("Ingrese kilometros recorridos:\n"))
            autoNuevo = Principal.Auto(marca=marca, modelo=modelo, año=año, precio_por_kilometro=precio_por_kilometro, seguro_alquiler=seguro_alquiler, dni_cliente=dni_cliente, nombre_del_arrendatario=nombre_del_arrendatario, kilometros_recorridos=kilmetros_recorridos)
            lista.append(autoNuevo)

        elif (opc == 2):
            for recorrer in lista:
                recorrer.mostrarDatos()
        elif (opc == 3):
            break


menu()