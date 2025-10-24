# Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 
def convertir_decimal_a_bianario(base_10:int)->str:
    if base_10 == 0:
        return ''
    return convertir_decimal_a_bianario(base_10//2) + str(base_10%2)