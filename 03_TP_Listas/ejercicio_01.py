# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

import sys

notas_alumnos = [8,2,10,2,5,7,9,9,4,10]
acumulador_notas = 0
mayor_nota = -sys.maxsize -1 
menor_nota = sys.maxsize
total_alumnos = len(notas_alumnos)

print("Estas son todas las notas de los alunos")
for posicion,nota in enumerate(notas_alumnos):
    acumulador_notas += nota
    if nota > mayor_nota:
        mayor_nota = nota
    if nota < menor_nota:
        menor_nota = nota    
    print(f"{posicion + 1:>2}°. {nota}")

promedio = acumulador_notas / total_alumnos
print(f"El promedio de notas es de {promedio} pts")
print(f"La nota mas alta es de {mayor_nota} pts")
print(f"La nota mas baja es de {menor_nota} pts")
