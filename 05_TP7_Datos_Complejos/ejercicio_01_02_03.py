from colecciones import *
from entrada_de_datos import *

# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200 
precios_frutas['Manzana'] = 1500 
precios_frutas['Pera'] = 2300
dibujar_titulo('Ejercicio 01',tab=1,char='=',cant=5)
mostrar_dicc(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800
precios_frutas['Banana'] = 1330 
precios_frutas['Manzana'] = 1700 
precios_frutas['Melon'] = 2800
dibujar_titulo('Ejercicio 02',tab=1,char='=',cant=5)
mostrar_dicc(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 
frutas = precios_frutas.keys()
dibujar_titulo('Ejercicio 03',tab=1,char='=',cant=5)
mostrar_lista(frutas)