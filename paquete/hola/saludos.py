class Saludo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def saludar(self):
            print("Hola, soy ", self.nombre)