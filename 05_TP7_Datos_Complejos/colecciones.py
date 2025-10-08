# ===== LISTAS =====
def mostrar_lista(lista:list):
    """
    Muestra los elementos de una lista en forma enumerada
    Parámetros:
        lista (list): Lista de elementos a mostrar.
    Retorno:
        None
    """ 
    print()
    for i, elemento in enumerate(lista,start=1):
        print(f"{i:>3}. {elemento:<50}")

# ===== DICCIONARIOS =====
def mostrar_dicc(dicc:dict):
    for i,(k,v) in enumerate(dicc.items(),start=1):
        print(f"{i:>3}. {k:<15} {v:>8}")
