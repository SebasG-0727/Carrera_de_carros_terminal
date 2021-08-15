from pista import Pista
from jugador import Jugador
import os


class Juego:
  
  def __init__(self,nombre):
    self.nombre = nombre
    self.jugador = Jugador()
    
    
    
  def mostrar_portada(self):
      print("----------------------------")
      print("      Carrera de carros")
      print("---------------------------")
      print("1. Pista Monaco")
      print("2. Pista Monza")
      print("3. pista Reims")
      print()
      opcion = ""
      while opcion not in("1","2","3"):
        opcion = input("    -->")
      return opcion

  def crear_pistas(self):
    os.system("clear")
    opcion =self.mostrar_portada()
    if opcion == "1":
        pista = Pista("Monaco",8,40,"-")
    elif opcion == "2":
        pista = Pista("Monza",10,45,".")
    elif opcion == "3":
        pista = Pista("Reims",6,50,"-")
    return pista


  

      
    
  

  
