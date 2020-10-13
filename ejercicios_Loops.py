
def ejercicio_1_for_en_vector():
    nombres = ["Lucas", "Franco", "Luciano", "Malena", "Jonatan", "Luciano", "Rodrigo", "Maria Sol", "Enzo", "Milena"]
    for nom in nombres:
        print(nom)

print(ejercicio_1_for_en_vector())


def ejercicio_2_for_en_vector():
    nombres = ["Lucas", "Franco", "Luciano", "Malena", "Jonatan", "Luciano", "Rodrigo", "Maria Sol", "Enzo", "Milena"]
    for i in range(0, 11):
        print(f"{nombres[i]} {i}")


print(ejercicio_2_for_en_vector())

def ejercicio_2_for_en_vector():
    rango=0
    nombres = ["Lucas","Franco","Luciano","Malena","Jonatan","Luciano","Rodrigo","Maria Sol","Enzo","Milena"]
    for recorrer in nombres:

        print(" En la posicion " + str(rango) + " se encuentra el valor " + recorrer)
        rango+=1

print(ejercicio_2_for_en_vector())

def ejercicio_3_for_en_vector():
    nombres = ["Lucas", "Franco", "Luciano", "Malena", "Jonatan", "Luciano", "Rodrigo", "Maria Sol", "Enzo", "Milena"]
    for i in nombres[4:]:
        print(i)
    print(f"El primer elemento es {nombres[1]}")

print(ejercicio_3_for_en_vector())



def ejercicio_4_while():
    nota = int(input("Ingrese nota"))
    contador = 1
    while (nota != 0):
        nuevanota = int(input("Ingrese una nueva nota, en caso de querer cancelar ingresar cero \n"))
        if (nuevanota == 0):
            total = nota / contador
            print(str(total))
            break
        elif (nuevanota != 0):
            nota += nuevanota
            contador += 1

print(ejercicio_4_while())
