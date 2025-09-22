# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
incio = 0
fin = 100
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(incio, fin):
    numero = int(input(f"Ingrese el {i+1}° numero {fin}: "))
    if numero != 0:        
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
        if numero > 0:
            positivos += 1
        else:
            negativos += 1
print(f"Se ingresaron {pares} numeros pares")
print(f"Se ingresaron {impares} numeros impares")
print(f"Se ingresaron {negativos} numeros negativos")
print(f"Se ingresaron {positivos} numeros positivos")