
import random
raund = 1


while True:
  print("*"* 10)
  print("Round", raund) 
  computador = random.randint(1, 3)
  usuario = int(input("Hola amigo, selecciona \n1 para piedra, \n2 para papel  \n3 para tigera \nElije el número==>"))
  

  def eleccion(numeroElegido):
    if numeroElegido == 1:
      return ("Piedra")
    elif numeroElegido == 2:
      return ("Papel")
    elif numeroElegido == 3:
      return ("Tijera")
    else:
      return ("elije bien hijo")
      
  def texto():
    print("Has elegido: " + eleccion(usuario))
    print("El Pc ha elegido: " + eleccion(computador))
    
  def textoNoEleccion():
    if eleccion(usuario) not in range(1, 4):
      print("Elige una opción correcta")

  def juego():
    if (usuario == 1 and computador == 3) or (
          usuario == 2 and computador == 1) or (usuario == 3 and computador == 2):
      texto()
      print("Has ganado, en hora buena")
    elif (usuario == 1 and computador == 1) or (
          usuario == 2 and computador == 2) or (usuario == 3 and computador == 3):
      texto()
      print("Han empatado")
    elif (usuario == 1 and computador == 2) or (usuario == 2 and computador == 3) or (usuario == 3 and computador == 1):
      texto()
      print("lo siento, has perdido")
    else:
      if usuario not in range(1, 3):
        textoNoEleccion()

  
  if raund == 7:
    break
  raund += 1
  juego()
  
  
  
