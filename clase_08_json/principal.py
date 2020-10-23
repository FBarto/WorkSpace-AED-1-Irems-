import json

from clase_08_json.usuarios import Usuario


def test_usuario():
    file_name = "./nuevo_archivo.json"
    usr = Usuario.generar_usuario()
    crear_archivo(file_name, usr.toJSON())


def test_json():
    usr = leer_archivo("./nuevo_archivo.json")
    print(usr)



def crear_archivo(nombre_archivo, datos):
    archivo = open(nombre_archivo, "w")
    archivo.write(str(datos))
    archivo.close()


def leer_archivo(nom):
    file = open(nom, "r")
    datos = json.load(file)
    print(datos)
    return datos


test_json()