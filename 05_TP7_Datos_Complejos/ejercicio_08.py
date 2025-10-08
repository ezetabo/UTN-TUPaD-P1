import entrada_de_datos as ed
import colecciones as cl

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 
productos_stock = {
    'pan': 20,
    'leche': 15,
    'huevos': 30,
    'azucar': 10,
    'yerba': 25
}
ed.dibujar_titulo('Stock inicial', char='=', cant=3)
cl.mostrar_dicc(productos_stock)
ed.dibujar_titulo('Manejo de stock', char='=', cant=3)
producto = ed.pedir_cadena('Ingrese el nombre del producto: ').lower()
cantidad = ed.pedir_entero('Ingrese la cantidad: ',minimo=1,maximo=10000)
if producto in productos_stock:
    productos_stock[producto] += cantidad
    print(f'Se actualizo el stock de \'{producto}\' en {productos_stock[producto]} unidades')
else:
    productos_stock[producto] = cantidad
    print(f'Se ingreso nuevo producto: \'{producto}\' con {productos_stock[producto]} unidades')
ed.dibujar_titulo('Stock actualizado', char='=', cant=3)
for producto, cantidad in productos_stock.items():
    print(f'{producto}: {cantidad} unidades')
