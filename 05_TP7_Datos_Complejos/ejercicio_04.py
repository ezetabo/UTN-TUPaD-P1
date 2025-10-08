import entrada_de_datos as ed
import colecciones as cl
# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 
agenda_telefonica = dict()
cantidad = 5
for i in range(cantidad):   
    while True:
        nombre = ed.pedir_cadena_solo_letras(f'Ingrese el {i+1}° de los {cantidad} nombres: ').lower()
        if nombre not in agenda_telefonica:
            agenda_telefonica[nombre] = None
            break
        print(f'*** ERROR *** El nombre {nombre} ya existe, ingrese uno diferente.')
    telefono = ed.pedir_cadena_solo_numeros(f'Ingrese el numero de telefono de {nombre}: ')
    agenda_telefonica[nombre] = telefono
ed.dibujar_titulo('agenda actual',char='=',cant=3)
cl.mostrar_dicc(agenda_telefonica)
ed.dibujar_titulo('buscar contacto',char='=',cant=3)
contacto = ed.pedir_cadena_solo_letras(f'Ingrese el nombre que quiere consultar: ').lower()
dato = agenda_telefonica.get(contacto,f'no existe en la agenda')
print(f'\nEl N° de telefono de {contacto}: {dato}\n')

