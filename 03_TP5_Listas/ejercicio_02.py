# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
'''
sorted(iterable, *, key=None, reverse=False)
Crea una copia de la lista pasada por parametro y la ordena segun los criterios pasados por parametros, 
si no se pasan criterios la ordena por default de menor a mayor
iterable: (obligatorio)cualquier objeto iterable (lista, tupla, diccionario, conjunto, etc.).
*: obliga al momemto de usar los parametros opcionales que deban ser nombrados.
key: (opcional)función que se aplica a cada elemento para extraer el valor por el cual se ordena.
reverse: (opcinal)si es True, ordena en orden descendente.
'''
productos = []
cantidad_ingresar = 5

for i in range(cantidad_ingresar):    
    producto = input(f"Ingrese el {i+1}° producto de {cantidad_ingresar}: ").lower()    
    # verifico que no exista dentro de la lista
    while producto in productos:
        print(f"El producto {producto} ya se encuentra dentro de la lista. Por favor ingrese uno distinto")
        producto = input(f"Ingrese el {i+1}° producto de {cantidad_ingresar}: ").lower()
    productos.append(producto)

print("\tLista de productos antes de ordenar") 
for posicion,producto in enumerate(productos):
    print(f"{posicion + 1}°. {producto}")
productos = sorted(productos)

print("\tLista de productos despues de ordenar") 
for posicion,producto in enumerate(productos):
    print(f"{posicion + 1}°. {producto}")
# pido el numero de posicion para usarlo como indice
posicion = int(input("Elija que numero de producto desea eliminar: "))
# valido que sea un rango valido
while posicion < 1 or posicion > len(productos) + 1:
    print(f"EL numero {posicion} no es valido")
    for posicion,producto in enumerate(productos):
        print(f"{posicion + 1}°. {producto}")
    posicion = int(input("Elija que numero de producto desea eliminar: "))
# uso el metodo pop para poder mostrar que elemnto se elimino
eliminado = productos.pop(posicion -1 )

print(f"El producto {eliminado} se elimino correctamente!!")

print("\tLista de productos") 
for posicion,producto in enumerate(productos):
    print(f"{posicion + 1}°. {producto}")