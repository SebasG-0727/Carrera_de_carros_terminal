from conductor import Conductor

class Carro:

    def __init__(self,nombre):
        self.nombre = nombre
        self.metro = 0

    def __str__(self):
        return self.nombre


    def avanzar(self):
        self.metro += Conductor.acelerar()
         
