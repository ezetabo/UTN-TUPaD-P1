#Creacion de un while infinito para que el usuario repita tantas veces como desee.
while True:
    #Listado del menu de opciones.
    print(f"\n{"*" * 25} Generador de Tabla de Verdad {"*" * 25}")
    print("Menu de opciones: ")
    print("1 - AND\n2 - OR\n3 - XOR\n4 - NAND\n5 - NOR\n6 - IMPLICA")
    print(" - Cualquier otra tecla para salir -")

    #Peticion de una opcion al usurio.
    opcion = input("Elija una operación lógica: ")

    #Analizo la opcion elegida por el usuario y genero el string para mostrar el nombre de la operacion.
    #Elegi el match ya que para multiples opciones de una misma variable es la mejor opcion.
    match opcion:
        case "1":
            operacion = "AND"
        case "2":
            operacion = "OR"
        case "3":
            operacion = "XOR"
        case "4":
            operacion = "NAND"
        case "5":
            operacion = "NOR"
        case "6":
            operacion = "IMPLICA"
        case _:
            #Opcion por default por si elige cualquier otro valor, uso el break para romper la iteracion del while.
            print("Fin del programa")
            break
    #Titulo con el nombre de la tabla que desea ver
    print(f"\nTabla de verdad para: {operacion}\n")
    #Encabezado con tabulaciones para que sea prolija la salida por consola.
    print("A\tB\tResultado")
    #Decorador para separar el encabezado de la creacion de la tabla
    print("-" * 25)

    #Para crear la comparacion utilizo dos for anidados con los dos posibles valores que pueden tomar cada variable
    #Bucle for con un array de dos valores representando la variable A
    for A in [True, False]:
        #Bucle for anidado con un array de dos valores representando la variable B
        for B in [True, False]:            
            #Analizo el valor de la operacion y realizo la operacion correspondiente.
            match operacion:
                case "AND":                    
                    resultado = A and B
                case "OR":                    
                    resultado = A or B
                case "XOR":
                    resultado = A != B
                case "NAND":
                    resultado = not (A and B)
                case "NOR":
                    resultado = not (A or B)
                case "IMPLICA":
                    '''ya que no hay un operador logico para esto, la forma mas facil es negar A y usar la disyuncion 
                    para que solo de falso con A=1 y B=0 esto hace que A se convierta a 0 y queda 0 or 0 = 0 y en todos los demas casos
                    o bien A es 1 o B es 1'''
                    resultado = (not A) or B
            #El print para armar cada combinacion y con las variables convertidas a int para que se vea 0 en vez de False y 1 en vez de True
            print(f"{int(A)}\t{int(B)}\t{int(resultado)}")    
