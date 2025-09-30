#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.
import math

def calcular_area_circulo(radio:float)->float:
    return math.pi * radio**2

def calcular_perimetro_circulo(radio:float)->float:
    return math.pi * radio