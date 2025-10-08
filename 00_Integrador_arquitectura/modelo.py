def crear_alumno(legajo, nombre, apellido, materia, nota_primer_parcial, nota_segundo_parcial, nota_tp_integrador):
    """
    Crea un diccionario que representa un alumno con sus notas y estado.
    
    Parámetros:
        legajo (str): Número de legajo del alumno.
        nombre (str): Nombre del alumno.
        apellido (str): Apellido del alumno.
        materia (str): Nombre de la materia.
        nota_primer_parcial (float): Nota del 1er parcial (0-10).
        nota_segundo_parcial (float): Nota del 2do parcial (0-10).
        nota_tp_integrador (float): Nota del trabajo integrador (0-10).
    
    Retorno:
        dict: Diccionario con los datos del alumno.
    """
    promedio = (nota_primer_parcial + nota_segundo_parcial + nota_tp_integrador) / 3
    estado_del_alumno = "APROBADO" if promedio >= 6 else "DESAPROBADO"

    return {
        "legajo": legajo,
        "nombre": nombre,
        "apellido": apellido,
        "materias": {
            "materia": materia,
            "nota_primer_parcial": nota_primer_parcial,
            "nota_segundo_parcial": nota_segundo_parcial,
            "nota_tp_integrador": nota_tp_integrador,
            "promedio": round(promedio, 2)
        },
        "estado_del_alumno": estado_del_alumno
    }
