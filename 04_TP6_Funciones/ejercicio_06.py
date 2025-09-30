#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero:int)->None:
    for i in range(1,11):
        print(f"{numero:>3} {"X":>3} {i:>3} {"=":>3} {numero*i:>3}")