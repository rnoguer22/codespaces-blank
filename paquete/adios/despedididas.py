def despedir():
    print("Adios")

class Despedida:
    def __init__(self, nombre):
        self.nombre = nombre
    def despedir(self):
        print("Adios ", self.nombre)