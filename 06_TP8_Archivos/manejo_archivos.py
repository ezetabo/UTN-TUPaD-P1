import os

ENCABEZADOS_ESPERADOS = ['nombre','precio','cantidad']

def existe_archivo(ruta:str)->bool:
    '''
    Recibe una str que representa la ruta de un archivo y verifica si existe.
    
    Parámetros:
        ruta (str): Ruta del archivo a verificar
    
    Retorno:
        True: si existe
        False: si no existe
    '''
    return os.path.exists(ruta)

def leer_txt(ruta: str,productos:list[dict]) -> tuple[bool,str]:
    '''    
    Lee un archivo de texto línea por línea y carga los datos en una lista de diccionarios.
	La primera línea del archivo debe contener los encabezados: nombre, precio, cantidad.
	
	Parámetros:
		ruta (str): Ruta del archivo de texto a leer.
		productos (list[dict]): Lista donde se cargarán los productos leídos.
		
    Retorno:
		tuple[bool, str]: Una tupla con un valor booleano indicando el éxito de la operación
		y un mensaje descriptivo del resultado.
    ''' 
    errores_conversion = []
    if not existe_archivo(ruta):
        return (False, f'El archivo \'{ruta}\' no existe.')
    if not ruta.lower().endswith('.txt'):
        return (False, 'El archivo seleccionado no es .txt')
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        if not lineas:            
            return (True, 'El archivo está vacío.')
        encabezados = lineas[0].strip().split(',')
        if encabezados != ENCABEZADOS_ESPERADOS: 
            return (False, f'Encabezados incorrectos. Se esperaban {ENCABEZADOS_ESPERADOS} pero se encontraron {encabezados}')
        for fila, linea in enumerate(lineas[1:], start=2):
            partes = linea.strip().split(',')
            if len(partes) != 3:
                errores_conversion.append(fila)
                continue
            nombre = partes[0].strip()
            precio = partes[1].strip()
            cantidad = partes[2].strip()
            if not precio.replace('.', '', 1).isdigit() or not cantidad.isdigit() or not nombre:
                errores_conversion.append(fila)
                continue            
            productos.append({'nombre': nombre,'precio': float(precio),'cantidad': int(cantidad)})
    if errores_conversion:
        mensaje = f'Carga parcial: {len(errores_conversion)} errores en filas {errores_conversion}'
    else:
        mensaje = 'Carga completada con éxito.'
    return (True, mensaje)

def escribir_txt(ruta: str, productos: list,*, modo: str = 'w'):
    '''
    Escribe en un archivo de texto los datos de una lista de diccionarios.
    Cada diccionario representa un producto con sus atributos.
    
    Parámetros:
        ruta (str): ruta del archivo de texto donde se escribirán los datos.
        productos (list): Lista de diccionarios con las claves 'nombre', 'precio' y 'cantidad'.
        modo (str, opcional): Modo de apertura del archivo.
            - 'w'(seleccion por defecto): Sobrescribe el archivo existente.
            - 'a': Agrega los nuevos datos al final del archivo.
    '''
    with open(ruta, modo, encoding='utf-8') as archivo:
        if modo == 'w':
            encabezado = ','.join(ENCABEZADOS_ESPERADOS)
            archivo.write(f'{encabezado}\n')
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            archivo.write(linea)
