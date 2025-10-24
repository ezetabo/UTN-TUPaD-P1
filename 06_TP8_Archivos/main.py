from funciones_generales import *
from manejo_archivos import *

ruta = ''
productos = []
menu_opciones = ['Cargar Archivo','Agregar prodcutos','Buscar producto','Actualizar producto','Mostrar productos','Salir']
while True:
    dibujar_titulo('Menú Pincipal',tab=1,char='=',cant=3)
    match pedir_opcion_listado('Seleccione una opcion: ',menu_opciones):
        case 1:
            dibujar_titulo('Cargar Archivo',tab=1,char='=',cant=3)
            if not ruta:
                while True:
                    ruta = 'productos.txt'
                    if pedir_opcion_listado('Seleccione una opcion: ', ['Usar archivo por default (productos.txt)','Ingresar una nueva ruta: ']) == 2:
                        ruta = pedir_cadena('Ingrese la ruta del archivo: ')                
                    exito,mensaje = leer_txt(ruta,productos)
                    dibujar_titulo(mensaje,char='-',cant=3)
                    if exito:                    
                        break
            else:
                dibujar_titulo('DENEGADO - Ya existe un archivo en uso',char='*',cant=3)
        case 2:
            dibujar_titulo('Agregar prodcutos',tab=1,char='=',cant=3)
            if not ruta:
                dibujar_titulo('DENEGADO - Debe cargar un archivo para poder operar',char='*',cant=3)
                continue
            escribir_txt(ruta,[crear_producto_consola(productos)],modo='a')
            dibujar_titulo('Creacion y carga exitosa',char='-',cant=3)
        case 3:
            dibujar_titulo('Buscar producto',tab=1,char='=',cant=3)
            if not productos:
                dibujar_titulo('DENEGADO - Debe tener productos para poder operar',char='*',cant=3)
                continue
            nombre = pedir_cadena('Ingrese el nombre del producto (parcial o completo): ')            
            mostrar_productos(buscar_prodcuto_por_nombre(productos,nombre))
        case 4:
            dibujar_titulo('Actualizar producto',tab=1,char='=',cant=3)
            if not productos:
                dibujar_titulo('DENEGADO - Debe tener productos para poder operar',char='*',cant=3)
                continue
            producto = pedir_un_producto('Seleccione el producto que quiere modificar: ',productos)
            opcion = pedir_opcion_listado('Seleccione que campo quiere modificar: ',['precio','cantidad'])
            if opcion == 1:            
                valor = pedir_flotante('Ingrese el nuevo precio: ',minimo=1)
                producto['precio'] = valor
            else:
                opcion = pedir_opcion_listado('Seleccione una opcion: ',['Agregar','Descontar','Nuevo valor'])
                valor = pedir_entero('Ingrese la cantidad de unidades: ',minimo=1)
                match opcion:
                    case 1:
                        producto['cantidad'] += valor
                    case 2:
                        producto['cantidad'] -= valor
                    case _:
                        producto['cantidad'] = valor
            actualizar_producto(producto,productos)
            escribir_txt(ruta,productos)
            dibujar_titulo('Actualizacion exitosa',char='-',cant=3)            
        case 5:
            dibujar_titulo('Mostrar productos',tab=1,char='=',cant=3)
            if not productos:
                dibujar_titulo('DENEGADO - Debe tener productos para poder operar',char='*',cant=3)
                continue
            mostrar_productos(productos)
        case _:
            dibujar_titulo('FIN DEL PROGRAMA',tab=1,char='=',cant=3)
            break


