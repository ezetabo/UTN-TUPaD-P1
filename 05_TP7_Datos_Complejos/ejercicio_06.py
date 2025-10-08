import entrada_de_datos as ed

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno
alumno_notas = dict()
cantidad_alumnos = 3
for i in range(cantidad_alumnos):   
    while True:
        alumno = ed.pedir_cadena_solo_letras(f'Ingrese el {i+1}° de los {cantidad_alumnos} alumnos: ').lower()
        if alumno not in alumno_notas:
            alumno_notas[alumno] = None
            break
        print(f'*** ERROR *** El alumno {alumno} ya existe, ingrese uno diferente.')
    nota_1 = ed.pedir_entero('Ingrese la primer nota: ',minimo=0,maximo=10)
    nota_2 = ed.pedir_entero('Ingrese la segunda nota: ',minimo=0,maximo=10)
    nota_3 = ed.pedir_entero('Ingrese la tercer nota: ',minimo=0,maximo=10)    
    alumno_notas[alumno] = (nota_1,nota_2,nota_3)
for alumno,notas in alumno_notas.items():
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    print(f'Alumno: {alumno}, promedio: {promedio:.2f}')