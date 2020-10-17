def cargarNota():
    lista =[]
    nombre = input("Ingrese nombre alumno ")
    nota = int(input("Ingrese nota "))
    lista=[nombre, nota]
    return lista


def recorrerNota(a):
    lista = a
    for i in lista:
        print(f"La nota es: {i[1]}")

def promocionados(a):
    lista=a
    for i in lista:
        if(i[1]>=7):
            print(f"El indice {lista.index(i)} La nota es: {i[1]} El alumno esta promocionado.")

def promedio(a):
    lista=a
    acu1=0
    acu2=0
    acu3=0
    cont=0
    for i in lista:
        if(i[1]<4):
            acu1+=1
        elif(i[1]>=7):
            acu3+=1
        elif (i[1] >= 4 & i[1] < 7):
            acu2 += 1
        cont += 1
    print(f"El %{str((100/cont)*acu1)} reprobo")
    print(f"El %{str((100/cont)*acu2)} es regular")
    print(f"El %{str((100/cont)*acu3)} esta promocionado")

def abanderados():
    alumnos={}
    i=0
    while(i!=3):
        nombre = input("Ingrese el nombre del Alumno: ")
        nota = float(input("Ingrese la nota del alumno: "))
        nuevo={nombre:nota}
        alumnos.update(nuevo)
        i+=1
    print(alumnos)



"""    lista=[["Franco",6],["Lucas",9],["Lucas",2]]
    promedio(lista)
    abanderados()"""