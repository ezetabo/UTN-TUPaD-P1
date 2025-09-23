from sys import maxsize, float_info

# ================================================ MANEJO DE LISTAS ================================================

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

def obtener_indice(elemento, lista: list[str]):
    """
    Busca un elemento en una lista y devuelve su índice.
    Parámetros:
        elemento (str): Elemento a buscar.
        lista (list[str]): Lista donde se busca el elemento.
    Retorno:
        int: Índice del elemento si se encuentra, -1 en caso contrario.
    """
    posicion = -1
    for i, elemento_lista in enumerate(lista):
        if elemento == elemento_lista:
            posicion = i
            break
    return posicion

def agregar_elemento(elemento, lista):
    """
    Agrega un elemento a la lista si no existe previamente.
    Parámetros:
        elemento (any): Elemento a agregar.
        lista (list): Lista donde se agregará el elemento.
    Retorno:
        bool: True si se agregó, False si ya estaba en la lista.
    """
    exito = False
    if elemento not in lista:
        lista.append(elemento)
        exito = True
    return exito

def agregar_por_indice(elemento, lista, posicion):
    """
    Reemplaza un elemento en la lista en una posición específica.
    Parámetros:
        elemento (any): Elemento a insertar.
        lista (list): Lista objetivo.
        posicion (int): Índice donde reemplazar el elemento.
    Retorno:
        bool: True si se reemplazó con éxito, False si la posición es inválida.
    """
    exito = False
    if posicion <= len(lista) and posicion >= 0:
        lista[posicion] = elemento
        exito = True
    return exito

def modificar_cantidad_por_indice(valor, lista, posicion, accion="+"):
    """
    Modifica un valor numérico en la lista en un índice dado.
    Parámetros:
        valor (int | float): Cantidad a sumar o restar.
        lista (list): Lista con valores numéricos.
        posicion (int): Índice del valor a modificar.
        accion (str, opcional): "+" para sumar, "-" para restar. Por defecto "+".
    Retorno:
        bool: True si la operación fue exitosa, False en caso contrario.
    """
    exito = False
    if posicion <= len(lista) and posicion >= 0:
        exito = True
        if accion == "+":
            lista[posicion] += valor
        else:
            lista[posicion] -= valor
            if lista[posicion] < 0:
                lista[posicion] = 0
    return exito

def mostrar_dos_listas(lista_uno, lista_dos,*,separador="=",cantidad=0):
    """
    Muestra dos listas en paralelo, emparejando elementos por índice,  opcionalmente con líneas separadoras
    antes y después de la lista.
    Parámetros:
        lista_uno (list): Primera lista (ejemplo: nombres).
        lista_dos (list): Segunda lista (ejemplo: valores asociados).
    Retorno:
        None
    """
    dibujar_separador(separador,cantidad)
    for i, nombre in enumerate(lista_uno):
        print(f"| {i+1:>3}. {nombre:<50} | {lista_dos[i]:>4} |")
    dibujar_separador(separador,cantidad)

def mostrar_dos_listas_por_condicion(lista_uno, lista_dos, condicion,*, de_que_lista=1):
    """
    Muestra los elementos de dos listas solo si cumplen una condición.
    Parámetros:
        lista_uno (list): Primera lista.
        lista_dos (list): Segunda lista.
        condicion (any): Valor que debe cumplirse para mostrarse.
        de_que_lista (int, opcional): 1 para comparar contra lista_uno, 2 para lista_dos. Por defecto 1.
    Retorno:
        None
    """
    for i, nombre in enumerate(lista_uno):
        if (lista_uno[i] == condicion and de_que_lista == 1) or (lista_dos[i] == condicion and de_que_lista == 2):
            print(f"{i+1}. {nombre} - {lista_dos[i]}")

def esta_vacia(lista):
    """
    Verifica si una lista está vacía.
    Parámetros:
        lista (list): Lista a evaluar.
    Retorno:
        bool: True si la lista está vacía, False si tiene elementos.
    """
    return len(lista) == 0

# ================================================ INGRESO DE DATOS ================================================

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