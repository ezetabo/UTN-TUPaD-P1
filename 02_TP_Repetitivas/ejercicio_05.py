# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
intentos = 1
numero_secreto = random.randint(0,9)
numero = int(input("Adivine el numero secreto entre 0 y 9: "))
while numero_secreto != numero:
    print("incorrecto!!")
    intentos += 1
    numero = int(input("Adivine el numero secreto entre 0 y 9: "))
print(f"Felicidades le llevo {intentos} intentos adivinar el numero {numero_secreto}")