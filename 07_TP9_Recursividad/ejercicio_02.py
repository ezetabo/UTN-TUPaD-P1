# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique.

def obtener_posicion_fibonacci(posicion:int)->int:
    match posicion:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return obtener_posicion_fibonacci(posicion-1) + obtener_posicion_fibonacci(posicion-2)