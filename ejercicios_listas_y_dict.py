"""
def ejercicio_1_cargar_lista():
    cont=0
    alumnos=[]
    while (cont!=10):
        alumnos.append(input("Ingrese nombre del alumnos"))
        cont+=1
    for i in alumnos:
        print("Alumno:"+i)

print(ejercicio_1_cargar_lista())
"""

"""
def ejercicio_2_modificar_lista():
    frutas =["manzana","pera","durazno"]
    verduras =["acelga", "lechuga"]

    frutas.insert(2,"tomate")
    print(f"{frutas}")

    verduras.extend(frutas)
    print(f"{verduras}")

    verduras.__delitem__(4)
    print(verduras)

    frutas.pop(-1)
    print(f"{frutas}")

print(ejercicio_2_modificar_lista())
"""
"""

def ejercicio_3_ordenar_y_buscar_lista():
    frutas = [1998,1989,1970,2020,1990]
    print(f"{frutas}")
    frutas.sort()
    print(f"{frutas}")
    a=int(input("Ingrese un año"))
    if a in frutas:
        print("El año ingresado esta en la lista")
    else:
        print("no esta en la listas.")
    print(f"1989 se encuentra en la posicion :{frutas.index(1989)}")
print(ejercicio_3_ordenar_y_buscar_lista())

"""

def jercicio_4_dicionarios():
    jugador = {'comida': 15, 'energia': 100, 'enemigos': 3}
    print(jugador.items())
    print(jugador.keys())
    nuevas_armas = {'rocas': 4, 'flechas': 5}
    jugador.update(nuevas_armas)
    print(jugador)
    nuevas_armas.setdefault('amigos', 10)
    print(jugador)
    jugador['comida']=30
    print(jugador)
    energia = jugador.get('energia')
    print(f"La energia es {energia}")

print(jercicio_4_dicionarios())