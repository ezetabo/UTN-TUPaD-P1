# escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"MEDIA: {media} - MEDIANA: {mediana} - MODA {moda}")
if media > mediana and mediana > moda:
    print("hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("hay sesgo negativo")
elif media == mediana and media == mean:
    print("no hay sesgo")
else:
    print("Los valores no cumplen el requisito para calcular el sesgo")