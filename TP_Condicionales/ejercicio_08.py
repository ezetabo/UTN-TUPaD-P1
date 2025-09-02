# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
mostrar = "Opcion incorrecta!!!"
nombre = input("Ingrese su nombre: ")
print("Elija una de las siguientes opciones: ")
print("1. Ver su nombre en mayúsculas.")
print("2. Ver su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion = int(input())
if opcion == 1:
    mostrar = nombre.upper()
elif opcion == 2:
    mostrar = nombre.lower()
elif opcion == 3:
    mostrar = nombre.title()
print(mostrar)