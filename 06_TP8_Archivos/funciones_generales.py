import unicodedata
from sys import maxsize, float_info

def pedir_cadena(mensaje:str, *, largo=50)->str:
    '''
    Solicita al usuario que ingrese una cadena válida.
    Parámetros:
        mensaje (str): Mensaje que se muestra al pedir la entrada.
        largo (int, opcional): Máximo de caracteres permitidos. Por defecto 50 caracteres.
    Retorno:
        str: Cadena ingresada válida.
    '''
    while True:
        cadena = input(mensaje).strip()
        if cadena.isspace():
            print('**ERROR** Debe ingresar un valor.')
            continue
        if len(cadena) > largo:
            print(f'**ERROR** Los datos ingresados NO deben superar los {largo} caracteres.')
            continue
        break
    return cadena

def pedir_cadena_solo_letras(mensaje:str, *, largo=50)->str:
    '''
    Solicita al usuario que ingrese una cadena válida (solo letras).
    Parámetros:
        mensaje (str): Mensaje que se muestra al pedir la entrada.
        largo (int, opcional): Máximo de caracteres permitidos. Por defecto 50 caracteres.
    Retorno:
        str: Cadena ingresada válida.
    '''
    while True:
        cadena = input(mensaje).strip()
        if not cadena.isalpha():
            print('**ERROR** Los datos ingresados deben ser solo letras.')
            continue
        if len(cadena) > largo:
            print(f'**ERROR** Los datos ingresados NO deben superar los {largo} caracteres.')
            continue
        break
    return cadena

def pedir_entero(mensaje:str, *, minimo=-maxsize-1, maximo=maxsize)->int:
    '''
    Solicita al usuario que ingrese un número entero dentro de un rango.
    Parámetros:
        mensaje (str): Mensaje a mostrar.
        minimo (int, opcional): Valor mínimo permitido. Por defecto es el mínimo negativo de un int.
        maximo (int, opcional): Valor máximo permitido. Por defecto es el máximo positivo de un int.
    Retorno:
        int: Número entero válido ingresado por el usuario.
    '''
    while True:
        negativo = False
        numero = input(mensaje).strip()
        if numero[0] == '-':
            negativo = True
            numero = numero.replace('-','')
        if not numero.isdigit():
            print('**ERROR** Los datos ingresados deben ser solo numericos.')
            continue
        numero = int(numero)
        if negativo:
            numero = numero * -1
        if numero < minimo or numero > maximo:
            print(f'**ERROR** El valor ingresado debe estar entre {minimo} y {maximo}.')
            continue
        break
    return numero

def pedir_flotante(mensaje:str, *, minimo=-float_info.max, maximo=float_info.max, precision=2)->float:
    '''
    Solicita al usuario que ingrese un número flotante válido dentro de un rango específico
    y lo redondea a una cantidad determinada de decimales.
    Parámetros:
        mensaje (str): Texto que se mostrará al usuario al pedir la entrada.
        minimo (float, opcional): Valor mínimo permitido. Por defecto es el mínimo negativo de un float.
        maximo (float, opcional): Valor máximo permitido. Por defecto es el máximo positivo de un float.
        precision (int, opcional): Cantidad de decimales a redondear. Por defecto es 2.
    Retorno:
        float: Número flotante válido ingresado por el usuario, redondeado según precision.
    '''
    while True:
        negativo = False
        numero = input(mensaje).strip()
        if numero[0] == '-':
            negativo = True
            numero = numero.replace('-','')      
        if numero.count('.') > 1 or not numero.replace('.','').isdigit():
            print('**ERROR** Los datos ingresados deben ser solo numericos y contener un solo (.).')
            continue
        numero = round(float(numero), precision)
        if negativo:
            numero = numero * -1
        if numero < round(minimo,precision) or numero > round(maximo,precision):
            print(f'**ERROR** El valor ingresado debe estar entre {round(minimo,precision)} y {round(maximo,precision)}.')
            continue
        break
    return numero

def pedir_nombre_unico(mensaje:str,productos:list[dict])->str:
    while True:
        nombre = pedir_cadena(mensaje)
        if existe_producto_en_lista(productos,nombre):
            print(f'\n **ERROR** \'{nombre}\' ya existe, debe ingresar uno nuevo!')
            continue
        return nombre

def dibujar_titulo(titulo:str,*,tab=0,char='=',cant=0):
    print(f'\n{'\t'*tab} {char*cant} {titulo.upper()} {char*cant}')

def normalizar_cadena(texto: str) -> str:
    '''
    Normaliza una cadena de texto eliminando acentos y convirtiéndola a minúsculas.
    
    Parámetros:
        texto (str): Cadena de texto a normalizar.
            
    Retorna:
        str: La cadena normalizada, en minúsculas y sin acentos.
    '''
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower()

def mostrar_lista(lista:list[dict]):
    '''
    Muestra los elementos de una lista en forma enumerada
    Parámetros:
        lista (list): Lista de elementos a mostrar.
    Retorno:
        None
    ''' 
    print()
    for i, elemento in enumerate(lista):
        print(f'{i+1:>3}. {elemento:<50}')

def pedir_opcion_listado(mensaje:str, listado:list[str])->int:
    '''
    Muestra un listado y solicita al usuario que seleccione una opción.
    Parámetros:
        mensaje (str): Texto que se mostrará al usuario al pedir la entrada.
        listado (list): Lista de opciones.
    Retorno:
        int: Opción seleccionada (entero dentro del rango válido).
    '''
    mostrar_lista(listado)
    return pedir_entero(mensaje, minimo=1, maximo=len(listado))

def buscar_prodcuto_por_nombre(productos:list[dict], nombre:str)->list[dict]:
    '''
    Busca productos por coincidencia exacta o parcial en una lista de diccionarios.
        
    Parámetros
    productos (list[dict]): Lista de productos representados como diccionarios.
    nombre (str): Nombre (o parte del nombre) del producto a buscar.
    
    Retorna
        
    list[dict]
        - Si encuentra una coincidencia exacta, devuelve una lista con un solo diccionario correspondiente a ese producto.
        - Si no hay coincidencia exacta, devuelve una lista con todos los productos cuyo nombre contenga la cadena buscada.
        - Si no encuentra ninguna coincidencia, devuelve una lista vacía.
    '''    
    encontrados = []
    for producto in productos:
        if normalizar_cadena(producto['nombre']) == normalizar_cadena(nombre):
            return [producto]            
        elif normalizar_cadena(producto['nombre']).startswith(normalizar_cadena(nombre)):
            encontrados.append(producto)    
    return encontrados

def actualizar_producto(producto_actualizado: dict, productos: list[dict]) -> bool:
    '''
    Actualiza la información de un producto existente dentro de la lista de productos.
        
    Parámetros:
        producto_actualizado (dict): Diccionario con los nuevos datos del producto.
        productos (list[dict]): Lista de productos.
        
    Retorna:
        True si el producto fue encontrado y actualizado correctamente, 
        False si no se encontró ningún producto con ese nombre.
    '''
    for i, producto in enumerate(productos):
        if normalizar_cadena(producto['nombre']) == normalizar_cadena(producto_actualizado['nombre']):
            productos[i] = producto_actualizado
        return True  
    return False

def existe_producto_en_lista(productos: list[dict], nombre: str)->bool:
    for producto in productos:
        if normalizar_cadena(producto['nombre']) == normalizar_cadena(nombre):
            return True
    return False

def crear_producto_consola(productos: list[dict])->dict:
    '''
    Permite crear un nuevo producto desde la consola mediante ingreso manual de datos, no acepta duplicados.
    
    Parámetros:
        productos (list[dict]): Lista de diccionarios que contiene los productos.
        
    Retorna:
        dict: el producto que fue creado y agregado correctamente a la lista.
    '''

    nombre = pedir_nombre_unico('Ingrese el nombre del producto: ',productos)
    precio = pedir_flotante('Ingrese el precio: ',minimo=1)
    cantidad = pedir_entero('Ingrese la cantidad de unidades: ',minimo=1)
    producto = {'nombre': nombre,'precio': precio,'cantidad': cantidad}
    productos.append(producto)
    return producto

def mostrar_productos(productos:list[dict]):
    if productos:
        print(f'•{'-'*81}•')
        for i,p in enumerate(productos,start=1):
            print(f'{'|'}{i:>3}{'|':>2} Producto: {p['nombre']:<20} {'|'} Precio: {p['precio']:>10} {'|'} Cantidad: {p['cantidad']:>10} {'|'}')
        print(f'•{'-'*81}•')
    else:
        dibujar_titulo('no hay datos para mostrar',char='-',cant=3)

def pedir_un_producto(mensaje:str,productos:list[dict])->dict:
    mostrar_productos(productos)
    posicion = pedir_entero(mensaje,minimo=1,maximo=len(productos))
    return productos[posicion-1]