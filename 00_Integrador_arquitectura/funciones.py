from sys import maxsize, float_info

def dibujar_separador(separador,cantidad):
    """
    Dibuja una línea repetida usando un carácter específico.
    Parámetros:
        separador (str): Carácter o cadena que se repetirá para dibujar la línea.
        cantidad (int): Número de veces que se repetirá el carácter.
    Retorno:
        None
    """
    print(f"{separador*cantidad}")

def mostrar_lista(lista,*,separador="=",cantidad=0):
    """
    Muestra los elementos de una lista en forma enumerada, opcionalmente con líneas separadoras
    antes y después de la lista.
    Parámetros:
        lista (list): Lista de elementos a mostrar.
    Retorno:
        None
    """
    dibujar_separador(separador,cantidad)
    for i, elemento in enumerate(lista):
        print(f"{i+1:>3}. {elemento:<50}")
    dibujar_separador(separador,cantidad)
    
def pedir_cadena(mensaje, *, largo=50):
    """
    Solicita al usuario que ingrese una cadena válida.
    Parámetros:
        mensaje (str): Mensaje que se muestra al pedir la entrada.
        largo (int, opcional): Máximo de caracteres permitidos. Por defecto 50 caracteres.
    Retorno:
        str: Cadena ingresada válida.
    """
    while True:
        cadena = input(mensaje).strip()
        if cadena.isspace():
            print("**ERROR** Debe ingresar un valor.")
            continue
        if len(cadena) > largo:
            print(f"**ERROR** Los datos ingresados NO deben superar los {largo} caracteres.")
            continue
        break
    return cadena

def pedir_cadena_solo_letras(mensaje, *, largo=50):
    """
    Solicita al usuario que ingrese una cadena válida (solo letras).
    Parámetros:
        mensaje (str): Mensaje que se muestra al pedir la entrada.
        largo (int, opcional): Máximo de caracteres permitidos. Por defecto 50 caracteres.
    Retorno:
        str: Cadena ingresada válida.
    """
    while True:
        cadena = input(mensaje).strip()
        if not cadena.isalpha():
            print("**ERROR** Los datos ingresados deben ser solo letras.")
            continue
        if len(cadena) > largo:
            print(f"**ERROR** Los datos ingresados NO deben superar los {largo} caracteres.")
            continue
        break
    return cadena

def pedir_entero(mensaje, *, minimo=-maxsize-1, maximo=maxsize):
    """
    Solicita al usuario que ingrese un número entero dentro de un rango.
    Parámetros:
        mensaje (str): Mensaje a mostrar.
        minimo (int, opcional): Valor mínimo permitido. Por defecto es el mínimo negativo de un int.
        maximo (int, opcional): Valor máximo permitido. Por defecto es el máximo positivo de un int.
    Retorno:
        int: Número entero válido ingresado por el usuario.
    """
    while True:
        numero = input(mensaje).strip()
        if not numero.isdigit():
            print("**ERROR** Los datos ingresados deben ser solo numericos.")
            continue
        numero = int(numero)
        if numero < minimo or numero > maximo:
            print(f"**ERROR** El valor ingresado debe estar entre {minimo} y {maximo}.")
            continue
        break
    return numero

def pedir_flotante(mensaje, *, minimo=-float_info.max, maximo=float_info.max, precision=2):
    """
    Solicita al usuario que ingrese un número flotante válido dentro de un rango específico
    y lo redondea a una cantidad determinada de decimales.
    Parámetros:
        mensaje (str): Texto que se mostrará al usuario al pedir la entrada.
        minimo (float, opcional): Valor mínimo permitido. Por defecto es el mínimo negativo de un float.
        maximo (float, opcional): Valor máximo permitido. Por defecto es el máximo positivo de un float.
        precision (int, opcional): Cantidad de decimales a redondear. Por defecto es 2.
    Retorno:
        float: Número flotante válido ingresado por el usuario, redondeado según precision.
    """
    while True:
        numero = input(mensaje).strip()        
        if numero.count('.') > 1 or not numero.replace('.','').isdigit():
            print("**ERROR** Los datos ingresados deben ser solo numericos y contener un solo (.).")
            continue
        numero = round(float(numero), precision)
        if numero < round(minimo,precision) or numero > round(maximo,precision):
            print(f"**ERROR** El valor ingresado debe estar entre {round(minimo,precision)} y {round(maximo,precision)}.")
            continue
        break
    return numero

def pedir_opcion_listado(mensaje, listado):
    """
    Muestra un listado y solicita al usuario que seleccione una opción.
    Parámetros:
        mensaje (str): Texto que se mostrará al usuario al pedir la entrada.
        listado (list): Lista de opciones.
    Retorno:
        int: Opción seleccionada (entero dentro del rango válido).
    """
    mostrar_lista(listado)
    return pedir_entero(mensaje, minimo=1, maximo=len(listado))