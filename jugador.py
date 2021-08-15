class Jugador:
  def __init__(self):
    self.identificador = " "

  def __str__(self):
    return self.identificador

  def elegir_carro(self):
    self.identificador = input("Elige un Carro y pulsa (Enter)...  ")
    