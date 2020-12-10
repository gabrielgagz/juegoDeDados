from random import randrange

def playAgain():
    input("Presioná ENTER para tirar los dados nuevamente.")
    throwDice()

def throwDice():
    result = randrange(1,6)+randrange(1,6) # Cada rango representa un dado
    if (result == 4):
        print("\nLa suma de los dados es " + str(result) + ".¡Has ganado la partida!")
    elif (result > 4):
        print("\nLa suma de los dados es " + str(result) + ". Debes volver a intentarlo.")
        playAgain()
    else:
        print("\nLa suma de los dados es "+ str(result) + ". Lamentablemente has perdido la partida.")
        
# Mensaje de bienvenida. Solo se muestra al inicio        
input("\n" \
    "!Bienvenid@ al juego! \n" \
    "Consiste en tirar dos dados y obtener la suma de ambos. \n" \
    "Ganarás si el resutado es 4. \n" \
    "Perderás si el resultado es menor a 4. \n" \
    "Volverás a tirar los dados si el resultado es mayor que 4. \n" \
    "Por favor presioná ENTER para continuar.")

throwDice() # Iniciamos el script
