from ejercicio_01 import *
from ejercicio_02 import *
from ejercicio_03 import *
from ejercicio_04 import *
from ejercicio_05 import *
from ejercicio_06 import *
from ejercicio_07 import *
from ejercicio_08 import *
from ejercicio_09 import *
from ejercicio_10 import *

print("\n================== EJ 01 ==================\n")
imprimir_hola_mundo()

print("\n================== EJ 02 ==================\n")
print(saludar_usuario(input("Inrese su nombre: ")))

print("\n================== EJ 03 ==================\n")
informacion_personal(input("Inrese su nombre: "),input("Inrese su apellido: "),int(input("Inrese su edad: ")),input("Inrese su residencia: "))

print("\n================== EJ 04 ==================\n")
radio = float(input("Ingrese el radio del circulo: "))
print(f"El area de un circulo con radio {radio} es de {calcular_area_circulo(radio):.2f}")
print(f"El perimetro de un circulo con radio {radio} es de {calcular_perimetro_circulo(radio):.2f}")

print("\n================== EJ 05 ==================\n")
print(f"Los segundos ingresados corresponden a {segundos_a_horas(int(input("Ingrese la cantidad de segundos: "))):.2f} hora/s")

print("\n================== EJ 06 ==================\n")
tabla_multiplicar(int(input("Ingrese el numero de la tabla que quiere ver: ")))

print("\n================== EJ 07 ==================\n")
a = int(input("Ingrese el primer operando: "))
b= int(input("Ingrese el primer operando: "))
resultado = operaciones_basicas(a, b)
print(f"{a} + {b} = {resultado[0]}")
print(f"{a} - {b} = {resultado[1]}")
print(f"{a} * {b} = {resultado[2]}")
print(f"{a} / {b} = {resultado[3]}")

print("\n================== EJ 08 ==================\n")
print(f"Su indice de masa corporal es: {calcular_imc(float(input("Ingrese su peso en kilogramos: ")),float(input("Ingrese su altura en metros: "))):.2f}")

print("\n================== EJ 09 ==================\n")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius):.2f}°F")

print("\n================== EJ 10 ==================\n")
print(f"El promedio de los numero ingresados es {calcular_promedio(float(input("Ingrese el 1° numero de 3: ")),float(input("Ingrese el 2° numero de 3: ")),float(input("Ingrese el 2° numero de 3: "))):.2f}")