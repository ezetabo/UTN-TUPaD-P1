from funciones import *

opciones = ["Ingresar titulo (sin ejemplares)",
            "Ingresar ejemplares disponibles (sin titulo)",
            "Mostrar catalogo",
            "Consultar disponibilidad de un titulo especifico",
            "Listar agotados",
            "Igresar titulo (con ejemplares)",
            "Actualizar ejemplares (prestamo/devolucion)",
            "ver catalogo completo",
            "Salir"]
titulos = []
ejemplares = []

while True:
    match pedir_opcion_listado("Elija una opcion: ",opciones):
        case 1:
            print("\t Ingresar titulo (sin ejemplares)")
            while True:
                titulo = pedir_cadena("Ingrese el titulo del libro que desea agregar: ")
                if agregar_elemento(titulo,titulos):
                    print("Titulo agregado correctamente")
                    ejemplares.append(0)
                    break
                else:
                    print("**ERROR** Ese titulo ya se existe, por favor ingrese uno nuevo")
                    continue                
        case 2:
            print("\t Ingresar ejemplares disponibles (sin titulo)")
            titulo = pedir_opcion_listado("Elija a que titulo le quiere agregar ejemplares: ",titulos)
            cantidad = pedir_entero("Ingrese la cantidad de ejemplares: ",minimo=1,maximo=100)
            agregar_por_indice(cantidad,ejemplares,titulo-1)
        case 3:
            print("\t Mostrar catalogo")
            mostrar_lista(titulos,cantidad=50)
        case 4:
            print("\t Consultar disponibilidad de un titulo especifico")
            titulo = pedir_opcion_listado("Elija a que titulo le quiere consultar: ",titulos)
            nombre = obtener_indice(titulos,titulo-1)
            mostrar_dos_listas_por_condicion(titulos,ejemplares,nombre)
            
        case 5:
            print("\t Listar agotados")
            mostrar_dos_listas_por_condicion(titulos,ejemplares,0,2)
        case 6:
            print("\t Igresar titulo (con ejemplares)")
            while True:
                titulo = pedir_cadena("Ingrese el titulo del libro que desea agregar: ")
                if agregar_elemento(titulo,titulos):
                    cantidad = pedir_entero("Ingrese la cantidad de ejemplares: ",minimo=1,maximo=100)
                    ejemplares.append(cantidad)
                    print("Titulo agregado correctamente")
                    break
                else:
                    print("**ERROR** Ese titulo ya se existe, por favor ingrese uno nuevo")
                    continue                
        case 7:
            print("\t Actualizar ejemplares (prestamo/devolucion)")
        case 8:
            print("\t ver catalogo completo")
        case _:
            print("\t<<< Fin del programa >>>")
            break

