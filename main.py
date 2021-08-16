from carro import Carro
from pista import Pista
from juego import Juego
from jugador import Jugador
import random
import os
import time
from io import open




archivo_texto=open("datos.txt","w")

jugador = Jugador()
juego = Juego("Apuesta de carros")
juego.mostrar_portada()

#flujo del programa

os.system("clear")


pista = juego.crear_pistas()

os.system("clear")

pista.poner_carros()
pista.mostrar_pista()
jugador.elegir_carro()

while True:

    os.system("clear")
    ganadores = pista.comprobar_ganadores()
    if len (ganadores) > 0:
        break

    pista.poner_ornamento()
    pista.avanzar_carros()
    pista.poner_carros()
    pista.mostrar_pista()

    time.sleep(1)

pista.mostrar_pista()
pista.mostrar_podio()

#Guardar archivos
def guardar_puntajes(nombre_archivo,ganadores):
  archivo = open(nombre_archivo, "w")
  for carro in ganadores:
    archivo.write("los ganadores son los carros:" + str(carro)+"\n")
  archivo.close()

def recuperar_puntajes(nombre_archivo):
  puntajes = []
  archivo = open(nombre_archivo, "r")
  for línea in archivo:
      nombre = línea.rstrip("\\n").split(",")
      puntajes.append((nombre))
  archivo.close()
  return puntajes

guardar_puntajes("datos.txt",ganadores)








