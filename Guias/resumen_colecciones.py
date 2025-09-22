# Resumen de Colecciones en Python

# ------------------ LISTAS ------------------
lista = [10, 20, 30, 40]
print("Lista inicial:", lista)

# Acceder
print("Elemento en índice 1:", lista[1])

# Modificar
lista[2] = 99
print("Lista modificada:", lista)

# Agregar
lista.append(50)
print("Lista después de append:", lista)

# Eliminar por valor
lista.remove(20)
print("Lista después de remove:", lista)

# pop() elimina por índice y devuelve el valor
valor = lista.pop(1)
print("Valor eliminado con pop:", valor)
print("Lista después de pop:", lista)

# del lista[0]
# lista = [elemento for elemento in lista if elemento != valor]
# lista.clear()


# ------------------ TUPLAS ------------------
tupla = (1, 2, 3, 4)
print("\nTupla inicial:", tupla)

# Acceder
print("Elemento en índice 2:", tupla[2])

# ⚠️ No se pueden modificar, agregar ni eliminar elementos


# ------------------ SETS ------------------
conjunto = {1, 2, 3, 4}
print("\nSet inicial:", conjunto)

# Acceder → no se puede por índice, pero se puede recorrer
for elem in conjunto:
    print("Elemento en set:", elem)

# Agregar
conjunto.add(5)
print("Set después de add:", conjunto)

# Eliminar
conjunto.remove(3)
print("Set después de remove:", conjunto)

# pop() elimina y retorna un elemento arbitrario
valor_set = conjunto.pop()
print("Valor eliminado con pop:", valor_set)
print("Set después de pop:", conjunto)

#remove() → elimina por valor, da error si no existe.
#discard() → elimina por valor, no da error si no existe.
#pop() → elimina y devuelve un elemento cualquiera (arbitrario, no por índice).
# ------------------ DICCIONARIOS ------------------
diccionario = {"a": 1, "b": 2, "c": 3}
print("\nDiccionario inicial:", diccionario)

# Acceder
print("Valor de clave 'b':", diccionario["b"])

# Modificar
diccionario["b"] = 20
print("Diccionario modificado:", diccionario)

# Agregar
diccionario["d"] = 4
print("Diccionario después de agregar:", diccionario)

# Eliminar con pop() retorna el valor borrado
valor_dic = diccionario.pop("a")
print("Valor eliminado con pop:", valor_dic)
print("Diccionario después de pop:", diccionario)


# ------------------ ARRAYS ------------------
from array import array

arr = array("i", [1, 2, 3, 4])
print("\nArray inicial:", arr)

# Acceder
print("Elemento en índice 2:", arr[2])

# Modificar
arr[1] = 99
print("Array modificado:", arr)

# Agregar
arr.append(5)
print("Array después de append:", arr)

# Eliminar
valor_arr = arr.pop(0)
print("Valor eliminado con pop:", valor_arr)
print("Array después de pop:", arr)
