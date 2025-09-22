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
    mostrar_lista(opciones)
    opcion = input("Elija una opcion: ")
    match opcion:
        case "1":
            print("\t Ingresar titulo (sin ejemplares)")
        case "2":
            print("\t Ingresar ejemplares disponibles (sin titulo)")
        case "3":
            print("\t Mostrar catalogo")
        case "4":
            print("\t Consultar disponibilidad de un titulo especifico")
        case "5":
            print("\t Listar agotados")
        case "6":
            print("\t Igresar titulo (con ejemplares)")
        case "7":
            print("\t Actualizar ejemplares (prestamo/devolucion)")
        case "8":
            print("\t ver catalogo completo")
        case "9":
            print("\t<<< Fin del programa >>>")
            break
        case _:
            print("\t***La opcion seleccionada no es valida***")
'''titulos = ["El señor de los anillos", "Orgullo y prejuicio","Matar un ruiseñor"]
ejemplares = [5,3,7]

while True:
    print("menú de opciones:")
    print("1.Ingresar titulos. \n2.Ingresar ejemplares. \n3.Mostrar catálago. \n4.Consultar disponibilidad. \n5.Listar agotados.")
    print("6.Agregar Título. \n7.Actualizar ejemplares (préstamo/devolución). \n8.Salir")
    opcion = input("Seleccione una de las opciones: ")
    match opcion:
        case "1":
            print("\t Ingreso de Titulo")
        case "2":
            print("\t Ingreso de Ejemplar")
        case "3":
            print("\t Mostrar Catalogo")
        case "4":
            print("\t Consultar Disponibles")
        case "5":
            print("\t Lista de agotados")
        case "6":
            print("\t Agregar")
        case "7":
            print("")
        case "8":
            print("\t<<< Fin del programa >>>")
            break
        case _:
            print("\t***La opcion seleccionada no es valida***")
'''