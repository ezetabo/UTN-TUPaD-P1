from ejercicio_01 import *
from ejercicio_02 import *
from ejercicio_03 import *
from ejercicio_04 import *
from ejercicio_05 import *
from ejercicio_06 import *
from ejercicio_07 import *
from ejercicio_08 import *

numero = 23
potencia = 3
palabra = 'Anita lava la tina'
digitos = 8546
bloques = 650
numero_repetidos = 12233421
digito = 2
# === EJ 01 ===
print(f'El factorial de {numero} es: {calcular_factorial(numero)}')
# === EJ 02 ===
print(f'La posicion {numero} de fibonacci es: {obtener_posicion_fibonacci(numero)}')
# === EJ 03 ===
print(f'{numero} elevado a la {potencia} es: {calcular_potencia(numero,potencia)}')
# === EJ 04 ===
print(f'{numero}D es \'{convertir_decimal_a_bianario(numero)}\'B')
# === EJ 05 ===
if es_palindromo(palabra):
    print(f'\'{palabra}\' es palindromo')
else:
    print(f'\'{palabra}\' NO es palindromo')
# === EJ 06 ===
print(f'La suma de los digitos del numero {digitos} es: {sumar_digitos(digitos)}')
# === EJ 07 ===
print(f'Para construir una piramide con una base de {bloques} bloques, se prescisan: \'{contar_bloques(bloques)}\' bloques en total')
# === EJ 08 ===
print(f'El digito {digito} aparece {contar_digito(numero_repetidos,digito)} veces en el numero {numero_repetidos}')