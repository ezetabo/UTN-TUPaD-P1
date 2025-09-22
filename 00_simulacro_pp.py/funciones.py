def mostrar_lista(lista):
    for i, elemento in enumerate(lista):
        print(f"{i+1}. {elemento}")

def obtener_indice(elemento,lista:list[str]):
    posicion = -1
    for i, elemento_lista in lista:
        if elemento == elemento_lista:
            posicion = i
            break
    return posicion

def agregar_elemento(elemento,lista):
    exito = False
    if elemento not in lista:
        lista.append(elemento)
        exito = True
    return exito

def agregar_por_indice(elemento, lista, posicion):
    exito = False
    if posicion <= len(lista):
        lista[posicion] = elemento
        exito = True
    return exito

def modificar_cantidad_por_indice(valor, lista, posicion,accion="+"):
    exito = False
    if posicion <= len(lista):       
        exito = True
        if accion == "+":
            lista[posicion] += valor
        else:
            lista[posicion] -= valor
            if lista[posicion] < 0:
                lista[posicion] = 0
    return exito

def mostrar_dos_listas(lista_uno, lista_dos):
    for i, nombre in lista_uno:
        print(f"{i+1}. {nombre} - {lista_dos[i]}")

def mostrar_dos_listas_por_condicion(lista_uno, lista_dos, condicion, de_que_lista):
    for i, nombre in lista_uno:
        if (lista_uno[i] == condicion and de_que_lista == 1) or (lista_dos[i] == condicion and de_que_lista == 2):
            print(f"{i+1}. {nombre} - {lista_dos[i]}")

def esta_vacia(lista):
    return len(lista) > 0