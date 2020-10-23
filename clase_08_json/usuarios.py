import json
import uuid


class Usuario(json.JSONEncoder):

    def __init__(self, user_id, nombre, estado, dni, apellido):
        self.UserId = user_id
        self.Nombre = nombre
        self.Estado = estado
        self.Dni = dni
        self.Apellido = apellido

    @classmethod
    def generar_usuario(self):
        user_id = str(uuid.uuid4())
        nombre = input("ingrese su nombre")
        apellido = input("Ingrese su apellido")
        dni = int(input("Ingrese su DNI"))
        estado = input("Ingrese su estado")
        usuario = Usuario(user_id, nombre, estado, dni, apellido)
        return usuario

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)