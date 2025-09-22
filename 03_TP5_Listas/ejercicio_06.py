# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero).
lista = [5,2,8,1,6,3,10]
lista_rotada = []
'''
Con algoritmia
guardo el ultimo valor, luego recorro desde el final y voy subiendo de posicion cada elemento, por ultimo 
agrego el valor original de la la ultima posicion al princio. 
largo = len(lista)
ultimo = lista[-1]
for i in range( largo - 1, 0, -1):
    lista[i] = lista[i - 1] 
lista[0] = ultimo
'''
'''
Parecida la logica anterior, solo que aca no preciso rotar nada, solo saco el valor de la ultima posicion y lo inserto en la primera.
ultimo = lista.pop()
lista.insert(0,ultimo)
'''
'''
usando los temas actuales de slicing y concatenacion.
aplica la misma logica que los meteoos anteriores, obtengo el ultimo elemento y l convieto a lista y luego concateno el slicing de
la lista original con todos los elementos menos el ultimo
'''
lista_rotada = [lista[-1]] + lista[:-1]

print("Lista original")
for posicion,elemento in enumerate(lista):
    print(f"{posicion + 1}°. {elemento}")
print("Lista rotada")
for posicion,elemento in enumerate(lista_rotada):
    print(f"{posicion + 1}°. {elemento}")