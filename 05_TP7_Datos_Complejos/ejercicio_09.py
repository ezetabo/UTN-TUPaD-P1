import entrada_de_datos as ed
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora. 
dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo' ]
agenda = {
    ('lunes', '09:00'): 'reunion de equipo',
    ('lunes', '11:00'): 'llamada con cliente',
    ('lunes', '15:00'): 'revision de codigo',
    ('martes', '08:30'): 'entrenamiento semanal',
    ('martes', '13:00'): 'almuerzo con proveedores',
    ('miercoles', '10:00'): 'planificacion del sprint',
    ('miercoles', '14:30'): 'desarrollo de modulo principal',
    ('jueves', '09:00'): 'presentacion de avance',
    ('jueves', '16:00'): 'capacitacion interna',
    ('viernes', '12:00'): 'revision de incidencias',
    ('viernes', '17:00'): 'cierre semanal y reporte'
}
ed.dibujar_titulo('agenda actual',char='=',cant=3)
for (d,h),act in agenda.items():
    print(f'{d:<10} {h:<5} -> {act}')
ed.dibujar_titulo('consultar agenda',char='=',cant=3)
dia = ed.pedir_opcion_listado('Selecciones que dia quiere consultar: ',dias)
hora = ed.pedir_hora('Ingrese la hora que quiere consultar(HH:MM): ')
actividad = agenda.get((dias[dia-1],hora),f'No hay actividades')
print(f'\nPara el {dias[dia-1]} a las {hora} -> {actividad}\n')