# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.
matriz = [[4,8,9],[2,5,3],[8,9,8],[10,2,5],[9,8,9]]
almunos_str = ['Juan', 'Pedro', 'Luis', 'Marcela', 'Micaela']
materias_str = ['Programacion', 'Arq. y S.O.', 'Matematica']
total_alumnos = len(matriz)
total_materias = len(matriz[0])
suma_por_materias = [0,0,0]
print(f"\t *** ALUMNOS ***")
for alumno,notas in enumerate(matriz):
    suma_notas = 0    
    for materia,nota in enumerate(notas):        
        suma_por_materias[materia] += nota
        suma_notas += nota
    promedio = suma_notas / total_materias
    print(f"El alumno {almunos_str[alumno]} tiene un promedio general de: {promedio:.2f}")
print(f"\n\t *** Materias ***")
for materia,acumulado in enumerate(suma_por_materias):
    promedio = acumulado / total_alumnos
    print(f"El promedio de la materia {materias_str[materia]} es de: {promedio}")