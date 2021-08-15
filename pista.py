from carro import Carro
from carril import Carril
from podio import Podio

class Pista:
    def __init__(self,nombre,filas,kilometros,ornamento):
        self.nombre = nombre
        self.filas = filas
        self.kilometros = kilometros
        self.ornamento = ornamento
        self.carriles = []
        self.traer_carriles()
        self.carros = []
        self.traer_carros()
    
    def traer_carriles(self):
      for i in range(self.filas):
            self.carriles.append([self.ornamento]* self.kilometros)
            
    def traer_carros(self):
      nombres = ["q","w","e","a","s","d","z","x","c","r"]
      for i in range(self.filas):
          carro = Carro(nombres[i])
          self.carros.append(carro)

    def avanzar_carros(self):
      for carro in self.carros:
        carro.avanzar()

    def poner_carros(self):
      for i in range(self.filas):
        self.carriles[i][self.carros[i].metro]= self.carros[i]
      
    def poner_ornamento(self):
      for i in range(self.filas):
        self.carriles[i][self.carros[i].metro]= self.ornamento
    
    def comprobar_ganadores(self):
      carros_ganadores = []
      for carro in self.carros:
        if carro.metro > self.kilometros - 5:
            carros_ganadores.append(carro)
      return carros_ganadores

    def mostrar_podio(self):
      print("Los ganadores son: \n")
      for carro in self.comprobar_ganadores():
        print(" ",carro,end=" ")
      print()
      Podio.imprimir_podio()
      print()
      return carro

    def mostrar_pista(self):
        print(" Pista de {}".format(self.nombre).center(self.kilometros))
        print(" ||SALIDA" + ("=" * ((self.kilometros)-14)) + " ||META")
        for i in range(self.filas):
            print(" ", end= " ")
            for j in range(self.kilometros):
                print(self.carriles[i][j],end="")
            print()

