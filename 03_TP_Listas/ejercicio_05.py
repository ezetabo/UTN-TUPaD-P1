# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.
estudiantes = ["ezequiel", "lucia", "martin", "sofia", "julian", "valentina", "tomas", "camila"]

print("\tLista de estudiantes") 
for posicion,elemento in enumerate(estudiantes):
    print(f"{posicion + 1}°. {elemento}")

print("Que accion desea realizar: \n 1. Eliminar \n 2. Agregar")
opcion  = int(input("Seleccione una opcion: "))

while opcion < 1 or opcion > 2:
    print(f"{opcion} no es una opcion valida. Por favor selecciona una opcion valida.")
    print("Que accion desea realizar: \n 1. Eliminar \n 2. Agregar")
    opcion  = int(input("Seleccione una opcion: "))

if opcion == 1:
    for posicion,elemento in enumerate(estudiantes):
        print(f"{posicion + 1}°. {elemento}")
    posicion = int(input("Elija que numero de estudiante deseas eliminar: "))    
    while posicion < 1 or posicion > len(estudiantes) + 1:
        print(f"EL numero {posicion} no es valido")
        for posicion,elemento in enumerate(estudiantes):
            print(f"{posicion + 1}°. {elemento}")
        posicion = int(input("Elija que numero de estudiante desea eliminar: "))
    eliminado = estudiantes.pop(posicion -1 )
    print(f"  operacion realizada con exito >>>{eliminado} se elimino de la lista<<<")
else:
    estudiante = input(f"Ingrese el nombre del estudiante que quiere agregar: ").lower()    
    while estudiante in estudiantes:
        print(f"El estudiante {estudiante} ya se encuentra dentro de la lista. Por favor ingrese uno distinto")
        estudiante = input(f"Ingrese el nombre del estudiante que quiere agregar: ").lower()
    estudiantes.append(estudiante)
    print(f"  operacion realizada con exito >>>{estudiante} se agrego a la lista<<<")

print("\tLista actualizada de estudiantes") 
for posicion,elemento in enumerate(estudiantes):
    print(f"{posicion + 1}°. {elemento}")