import entrada_de_datos as ed
# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
parcial_1 = {1,2,3,5,9,10}
parcial_2 = {2,5,6,7,8,10}

aprobaron_ambos = parcial_1 & parcial_2
aprobaron_solo_uno = parcial_1 ^ parcial_2
aprobaron_al_menos_uno = parcial_1 | parcial_2
ed.dibujar_titulo('Notas de ambos parciales',char='=',cant=3)
print(parcial_1)
print(parcial_2)
ed.dibujar_titulo('Los que aprobaron ambos parciales',char='=',cant=3)
print(aprobaron_ambos)
ed.dibujar_titulo('Los que aprobaron solo uno de los dos',char='=',cant=3)
print(aprobaron_solo_uno)
ed.dibujar_titulo('Los que aprobaron al menos un parcial',char='=',cant=3)
print(aprobaron_al_menos_uno)