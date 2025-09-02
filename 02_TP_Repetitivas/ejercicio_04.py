# Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.
numero = int(input("Ingrese numeros positivos para acumular su valor o cero para finalizar: "))
acumulado = 0
while numero != 0:
    acumulado += numero
    numero = int(input("Ingrese numeros positivos para acumular su valor o cero para finalizar: "))
print(f"El acumulado de los numeros ingresados es {acumulado}")