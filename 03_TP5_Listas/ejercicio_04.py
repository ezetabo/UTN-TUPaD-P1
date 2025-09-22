# 4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado

datos = [1,3,5,3,7,1,9,5,3]
datos_unicos = []
'''
la forma mas rapida es:
datos_unicos = list(set(datos))
'''
for dato in datos:
    if dato not in datos_unicos:
        datos_unicos.append(dato)

print(f"\t--- Lista de datos ---")
for i,item in enumerate(datos):
    print(f"{i+1}°. {item:>2}")

print(f"\t--- Lista de datos unicos ---")
for i,item in enumerate(datos_unicos):
    print(f"{i+1}°. {item:>2}")