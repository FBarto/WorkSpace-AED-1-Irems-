def mayorA10():
    n1= int(input("Ingrese un numero"))
    if ( n1 > 10 ):
        print(n1)
    else:
        print(f"{n1} Es menor a 10")

def tresNum(a,b,c):
    if ((a + b) == c ):
        print(f"La suma es igual al Tercero")
    else:
        print(f"La suma es distinta al Tercero")

def dosNum(d,f):
    if (d==f):
        return 1
    elif(d>f):
        (d*d)/(f*f)
    else:
        (f*f)/(d*d)

def celcius():
        f = int(input("Ingrese la temp en grados fahrenheit."))
        c = int((5 / 9) * (f - 32))
        return c