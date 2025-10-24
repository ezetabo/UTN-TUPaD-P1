# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 

def sumar_digitos(numero:int)->int:    
    if numero < 10:
        return numero    
    return (numero % 10) + sumar_digitos(numero // 10)
