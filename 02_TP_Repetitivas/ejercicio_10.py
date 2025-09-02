# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Ingrese un número entero: "))
calculo = numero
invertido = 0
if calculo < 0:
    calculo = calculo * -1
while calculo > 0:
    digito = calculo % 10
    invertido = invertido * 10 + digito
    calculo = calculo // 10
if numero < 0:
    invertido = invertido * -1
print(f"Numero ingresado {numero} - invertido {invertido}")