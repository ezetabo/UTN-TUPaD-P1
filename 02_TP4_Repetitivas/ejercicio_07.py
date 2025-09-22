# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.
inicio = 0
fin = int(input("Ingrese el un entero positivo: "))
suma = 0
for i in range(inicio, fin):
    suma += i
print(f"La suma desde {inicio} hasta {fin}, sin incluir el {inicio} y el {fin} es {suma}")