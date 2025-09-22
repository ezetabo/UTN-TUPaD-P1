# lista = [92,2,85,1,16,22,18,33,9,10]
lista = [1,2,9,10,18,16,22,33,85,92]

cantidad_elementos = len(lista)
cantidad_comparaciones = 0
for indice_pasada in range(cantidad_elementos-1):
    hizo_cambios = False
    for indice_actual in range(cantidad_elementos - 1 - indice_pasada):
        cantidad_comparaciones += 1
        if lista[indice_actual] > lista[indice_actual+1]:
            lista[indice_actual], lista[indice_actual+1] = lista[indice_actual+1], lista[indice_actual]
            hizo_cambios = True
    if not hizo_cambios:
        break

print(f"Cantidad de comparaciones: {cantidad_comparaciones}")