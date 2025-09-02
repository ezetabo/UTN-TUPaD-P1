# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 
cadena = input("Ingrese una frase o palabra:")
ultimo_char = cadena[len(cadena)-1]
if ultimo_char.lower() in "aeiou":
    cadena += "!"
print(cadena)