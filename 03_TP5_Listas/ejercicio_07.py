# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.
matriz =  [[12.5, 25.3], [10.2, 22.8], [14.1, 27.4], [9.6,  20.0], [11.7, 24.9], [13.3, 28.5], [8.4,  19.7]]
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
total_registros = len(matriz)
for i,dia in enumerate(matriz):
    suma_minimas += dia[0]
    suma_maximas += dia[1]
    amplitud_termina = dia[1] - dia[0]
    if i == 0 or amplitud_termina > mayor_amplitud:
        mayor_amplitud = amplitud_termina
        dia_mayor_amplitud = i
promedio_maximas = suma_maximas / total_registros
promedio_minimas = suma_minimas / total_registros
print(f"EL promedio de las temperaturas minimas es: {promedio_minimas:.2f}°C")
print(f"EL promedio de las temperaturas maximas es: {promedio_maximas:.2f}°C")
print(f"Con una diferencia de {mayor_amplitud}°C el dia {dias[dia_mayor_amplitud]} se registro la mayor amplitud termica")