# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

def calcular_factorial(numero:int)->int:
    if numero <= 1:
        return 1   
    return numero * calcular_factorial(numero-1)