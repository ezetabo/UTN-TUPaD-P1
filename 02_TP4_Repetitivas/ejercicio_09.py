# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 
incio = 0
fin = 100
acumulador = 0
for i in range(incio, fin):
    numero = int(input(f"Ingrese el {i+1}° numero {fin}: "))
    acumulador += numero
media = acumulador / fin
print(f"La media de los {fin} numeros ingresados es {media}")