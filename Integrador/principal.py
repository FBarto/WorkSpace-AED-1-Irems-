from Integrador import metodos

def menu():
    alumnos=[]
    a=False
    while (a!=0):
        print("ingrese opcion 1 para cargar notas \n "
              "ingrese opcion 2 para mostrar las notas cargadas \n "
              "ingrese opcion 3 para ver alumnos promocionados \n "
              "ingrese opcion 4 para ver los porcentajes de alumnos Promocionados, Regulares y Desaprobados\n "
              "ingrese opcion 5 para cargar los abanderados\n "
              "ingrese opcion 0 para salir del programa\n ")
        a=int(input("Ingrese la opcion deseada "))

        if (a == 1):
            alumnos.append(metodos.cargarNota())
        elif(a==2):
            metodos.recorrerNota(alumnos)
        elif(a==3):
            metodos.promocionados(alumnos)
        elif(a==4):
            metodos.promedio(alumnos)
        elif(a==5):
            metodos.abanderados()
        elif(a==0):
            a = True


menu()