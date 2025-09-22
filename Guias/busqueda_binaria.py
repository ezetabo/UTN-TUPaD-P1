
valor_buscado = 22 
# valor_buscado = 20 

lista = [1,2,9,10,18,16,22,33,85,92]

mensaje = f"El numero {valor_buscado} no se encuentra en la lista"
indice_inicio = 0
indice_final = len(lista)-1
indice_encontrado = -1
while (indice_inicio <= indice_final) and (indice_encontrado == -1) :
    indice_medio = (indice_inicio + indice_final) // 2
    if lista[indice_medio] == valor_buscado:
        indice_encontrado = indice_medio
    else:
        if lista[indice_medio] < valor_buscado:
            indice_inicio = indice_medio + 1
        else:
            indice_final = indice_medio -1

if indice_encontrado != -1:
    mensaje = f"El numero {valor_buscado} se encuentra en el indice {indice_medio}" 

print(mensaje)