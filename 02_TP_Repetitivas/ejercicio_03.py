# Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores
inicio = int(input("Ingrese el inicio del rango numerico:"))
fin = int(input("Ingrese el fin del rango numerico: "))
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print(f"La suma desde {inicio} hasta {fin}, sin incluir el {inicio} y el {fin} es {suma}")