#  Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
#      Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().

import unicodedata


def normalizar_cadena(texto: str) -> str:
    '''
    Normaliza una cadena de texto eliminando acentos y convirtiéndola a minúsculas.
    
    Parámetros:
        texto (str): Cadena de texto a normalizar.
            
    Retorna:
        str: La cadena normalizada, en minúsculas y sin acentos.
    '''
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower()

def es_palindromo(palabra:str)->bool:
    palabra = normalizar_cadena(palabra).replace(' ','').strip()
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
