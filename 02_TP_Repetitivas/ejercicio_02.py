# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.
numero = int(input("Ingrese un numero entero: "))
calculo = numero
digitos = 0
if calculo < 0:
    calculo = calculo * -1
while calculo > 0:
    calculo = calculo // 10
    digitos += 1
print(f"El numero {numero} tiene {digitos} digitos")