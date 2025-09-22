# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros = []
numeros_pares = []
numeros_impares = []
cantidad_numeros = 15

for i in range(cantidad_numeros):
    numeros.append(random.randint(1,100))
    
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
numeros_impares = [numero for numero in numeros if numero % 2 != 0]

print(f"\t--- Lista de numeros original ---")
for i,item in enumerate(numeros):
    print(f"{i+1:>2}°. {item:>3}")
print(f"Cantidad total: {len(numeros)}")

print(f"\t--- Lista de numeros pares ---")
for i,item in enumerate(numeros_pares):
    print(f"{i+1:>2}°. {item:>3}")
print(f"Cantidad total: {len(numeros_pares)}")

print(f"\t--- Lista de numeros impares ---")
for i,item in enumerate(numeros_impares):
    print(f"{i+1:>2}°. {item:>3}")
print(f"Cantidad total: {len(numeros_impares)}")