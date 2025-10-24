# Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general.

def calcular_potencia(base:int, exponente:int)->int:
    if exponente == 0:
        return 1
    return base * calcular_potencia(base,exponente-1)