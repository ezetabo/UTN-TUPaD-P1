#                 **********  TABOADA EZEQUIEL - PRIMER PARCIAL **********
# === Constantes para indentar prints en consola ===
SPACE_EJEMPLARES = 4
SPACE_CIERRE = 5
SPACE_TITULOS = 50
SPACE_NUM = 3

# === Formatos de consola ===
titulo_libro = f"|{"TITULO":>30} {"|":>27}"
stock_ejemplares = f"{"STOCK":>7}{"|":>3}"
apertura_encabezado_titulo = f"\n•{"-"*57}•"
cierre_encabezado_titulo = f"•{"-"*57}•"
apertura_encabezado_titulos_ejemplares = f"\n•{"-"*67}•"
cierre_encabezado_titulos_ejemplares = f"•{"-"*67}•"

# === Declaracion e inicializacion de variables ===
opciones = ["Ingresar titulo",
            "Ingresar ejemplares disponibles",
            "Mostrar catalogo",
            "Consultar disponibilidad de un titulo especifico",
            "Listar agotados",
            "Igresar titulo (con ejemplares)",
            "Actualizar ejemplares (prestamo/devolucion)",
            "Salir"]
accion = ["Prestamo","Devolucion"]
titulos = []
ejemplares = []

# === Valores de prueba (descoemntar para usar) ===
#titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor", "El Principito"]
#ejemplares = [5, 3, 7, 1]

# === Inicio del bucle principal ===
while True:
    print(f"\n {"="*7} MENU PRINCIPAL {"="*7}")
    
    # === Muestro listado de opciones del menu
    for i, elemento in enumerate(opciones):
        print(f"{i+1:>{SPACE_NUM}}. {elemento:<{SPACE_TITULOS}}")
    
    '''
    Pido el ingreso de un valor y verifico sea numerico y este dentro de los limites esperados, si no es asi pido el reingreso.
    Una validado lo convierto a entero.
    ********* ESTE PROCESO SE REPITE ********* 
    por este motivo en las proximas apariciones lo llamara "VALIDACION NUMERICA"
    '''
    while True:
            opcion_menu = input("Elija una opcion: ").strip()
            if not opcion_menu.isdigit():
                print("**ERROR** Los datos ingresados deben ser solo numericos.")
                continue
            opcion_menu = int(opcion_menu)
            if opcion_menu < 1 or opcion_menu > len(opciones):
                print(f"**ERROR** El valor ingresado debe estar entre {1} y {len(opciones)}.")
                continue
            break
        
# === Comienzo del match ===
    '''
    segun la opcion seleccionada realiza las operacion establecida
    '''   
    match opcion_menu:
        case 1:
            print("\n\t >> Ingresar titulos <<\n")
            
            while True:
                cantidad_titulos = input("Ingrese la cantidad de titulo que desea agregar: ").strip()
                if not cantidad_titulos.isdigit():
                    print("**ERROR** Los datos ingresados deben ser solo numericos.")
                    continue
                cantidad_titulos = int(cantidad_titulos)
                if cantidad_titulos < 1 :
                    print(f"**ERROR** El valor ingresado no puede ser 0 o negativo.")
                    continue
                break
            for i in range(0,cantidad_titulos):
                
                '''
                Elimino todos los espacios en blanco, tanto al principio como al final, verifico que no este vacia.
                Permito el ingreso de cualquier caracter ya que es un nombre de un titulo y este puede tener cualquier cosa.
                Una vez que la cadena este validada, me fijo si no esta dentro de la lista, si es asi lo informo y pido el reingreso
                repitiendo el proceso.
                ********* ESTE PROCESO SE REPITE ********* 
                por este motivo en las proximas apariciones lo llamare "VALIDACION DE TITULO"
                '''
                while True:
                    # creo un mensaje personalizado por si quiere ingresar 1 o varios
                    mensaje = "Ingrese el titulo que desea agregar: " if cantidad_titulos == 1 else f"Ingrese el {i+1}° de los {cantidad_titulos} titulos que desea agregar: "
                    nombre_titulo = input(mensaje).strip()
                    if nombre_titulo == "":
                        print("**ERROR** Debe ingresar un valor.")
                        continue  
                    elif nombre_titulo in titulos:
                        print(f"**ERROR** \"{nombre_titulo}\" ya existe, por favor ingrese uno nuevo")
                        continue
                    break
            
                '''
                Una vez que la cadena esta validada y no se encuentra en la lista lo agrego a la lista de titulos y agrego un nuevo elemento
                en la lista de ejemplares con valor de 0, podria utilizar el insert() con el mismo indice que el titulo pero no es necesario
                ya que si no se controla el correcto borrado de ambos elementos con el mismo indice y luego quiero agregar un elemento en 
                un indice que no existe dentro de la lista producira un error, asi que a esta altula es mas seguro usar append().
                Tampoco puedo usar la var i ya que solo seria util para cuando la lista de libro este, porque en otra circustancia estaria pisando los 
                indices ya que siempre empzaria por 0 y la cantidad-1 elegida por el usuario.
                '''
                titulos.append(nombre_titulo)
                ejemplares.append(0)
            mensaje = f"se agrego el titulo: \"{nombre_titulo}\"" if cantidad_titulos == 1 else f"se agregaron los {cantidad_titulos} titulos"
            print(f"\n --- Operacion exitosa, {mensaje} --- \n")
            
        case 2:
            print("\n\t >> Ingresar ejemplares disponibles <<")
            
            '''
            Antes de realizar cualquier tipo de interacion con las listas(que no sea agregar titulo) debo verificar que existan elementos en la 
            lista de titulos, si no es asi, informe el error y regreso al menu principal
            ********* ESTE PROCESO SE REPITE ********* 
            por este motivo en las proximas apariciones lo llamare "VALIDACION DE EXISTENCIA DE TITULOS"
            '''
            if not titulos:
                print("**ERROR** No existen titulos ingresados. Para agregar ejemplares deben existir titulos.")
                continue
            
            # === Muestro el listado de titulos existentes
            print(apertura_encabezado_titulo)
            print(titulo_libro)
            print(cierre_encabezado_titulo)
            for i, titulo in enumerate(titulos):
                print(f"| {i+1:>{SPACE_NUM}}. {titulo:<{SPACE_TITULOS}} |")
            print(cierre_encabezado_titulo)
            
            '''
            Debo pedir la eleccion de un titulo para agregarle ejemplares. Tenia dos opciones o lo hace mediante una cadena o usaba las
            posiciones a modo de indice, preferi usar la ocion de las posiciones ya que el usuario solo debe ingresar un valor numerico, 
            el cual esta controlado y dentro de un rango, con minimizo la cantidad de errores que puede cometer al ingresar una cadena.
            ********* ESTE PROCESO SE REPITE ********* 
            por este motivo en las proximas apariciones lo llamare "ELECCION DE TITULO EXISTENTE"
            '''
            while True:
                titulo_posicion = input("Elija a que titulo le quiere agregar ejemplares: ").strip()
                if not titulo_posicion.isdigit():
                    print("**ERROR** Los datos ingresados deben ser solo numericos.")
                    continue
                titulo_posicion = int(titulo_posicion)
                if titulo_posicion < 1 or titulo_posicion > len(titulos):
                    print(f"**ERROR** El valor ingresado debe estar entre {1} y {len(titulos)}.")
                    continue
                break
            
            # === VALIDACION NUMERICA ===
            while True:
                cantidad = input(f"ingrese la cantidad de ejemplares que quiere agregar \"{titulos[titulo_posicion-1]}\": ").strip()
                if not cantidad.isdigit():
                    print("**ERROR** Los datos ingresados deben ser solo numericos.")
                    continue
                cantidad = int(cantidad)
                if cantidad < 1 :
                    print(f"**ERROR** El valor ingresado no puede ser 0 o negativo.")
                    continue
                break
            
            '''
            Una vez que la cantidad esta validada se la sumo a la cantidad existente
            '''
            ejemplares[titulo_posicion-1] += cantidad
            
            print(f"\n --- Operacion exitosa, se agregaron {cantidad} ejemplares al titulo: \"{titulos[titulo_posicion-1]}\" --- \n")
            
        case 3:
            print("\n\t >> Mostrar catalogo <<")
            
            # === VALIDACION DE EXISTENCIA DE TITULOS ==
            if not titulos:
                print("**ERROR** No existen titulos ingresados. Para ver el catalogo deben existir titulos.")
                continue
            
            # === Muestro el listado de titulos existentes con sus ejemplares
            print(apertura_encabezado_titulos_ejemplares)
            print(f"{titulo_libro}{stock_ejemplares}")
            print(cierre_encabezado_titulos_ejemplares)
            for i, titulo in enumerate(titulos):
                print(f"| {i+1:>{SPACE_NUM}}. {titulo:<{SPACE_TITULOS}} | {ejemplares[i]:>{SPACE_EJEMPLARES}}{"|":>{SPACE_CIERRE}}")
            print(cierre_encabezado_titulos_ejemplares)
            
        case 4:
            print("\n\t >> Consultar disponibilidad de un titulo especifico <<\n")
            
            # === VALIDACION DE EXISTENCIA DE TITULOS ==
            if not titulos:
                print("**ERROR** No existen titulos ingresados. Para realizar consultas deben existir titulos.")
                continue
            
            # === Muestro el listado de titulos existentes con sus ejemplares
            print(apertura_encabezado_titulo)
            print(titulo_libro)
            print(cierre_encabezado_titulo)
            for i, titulo in enumerate(titulos):
                print(f"| {i+1:>{SPACE_NUM}}. {titulo:<{SPACE_TITULOS}} |")
            print(cierre_encabezado_titulo)
            
            # === ELECCION DE TITULO EXISTENTE ===
            while True:
                titulo_posicion = input("Elija que titulo desea consultar: ").strip()
                if not titulo_posicion.isdigit():
                    print("**ERROR** Los datos ingresados deben ser solo numericos.")
                    continue
                titulo_posicion = int(titulo_posicion)
                if titulo_posicion < 1 or titulo_posicion > len(titulos):
                    print(f"**ERROR** El valor ingresado debe estar entre {1} y {len(titulos)}.")
                    continue
                break         
            
            # === Muestro el titulo solicitado con sus ejemplares
            print(apertura_encabezado_titulos_ejemplares)
            print(f"{titulo_libro}{stock_ejemplares}")
            print(cierre_encabezado_titulos_ejemplares)
            print(f"| {titulo_posicion:>{SPACE_NUM}}. {titulos[titulo_posicion-1]:<{SPACE_TITULOS}} | {ejemplares[titulo_posicion-1]:>{SPACE_EJEMPLARES}}{"|":>{SPACE_CIERRE}}")
            print(cierre_encabezado_titulos_ejemplares)
            
        case 5:
            print("\n\t >> Listar agotados <<\n")
            
            # === VALIDACION DE EXISTENCIA DE TITULOS ===
            if not titulos:
                print("**ERROR** No existen titulos ingresados. Para realizar consultas deben existir titulos.")
                continue
            
            '''
            Verifico que en el listado de ejemplares haya por los menos un elemento con valor 0, si no es asi lo informo, una vez que haya
            encontrado por lo menos uno, muestro el titulo con sus ejemplares siempre y cuando el valor del ejemplar sea 0
            '''
            if ejemplares.count(0) < 1:                
                print("Ningun Titulo se encuentra agotado")
            else:
                print(apertura_encabezado_titulos_ejemplares)
                print(f"{titulo_libro}{stock_ejemplares}")
                print(cierre_encabezado_titulos_ejemplares)
                for i, titulo in enumerate(titulos):                    
                    if ejemplares[i] == 0:
                        print(f"| {" ":>{SPACE_NUM}}. {titulo:<{SPACE_TITULOS}} | {ejemplares[i]:>{SPACE_EJEMPLARES}}{"|":>{SPACE_CIERRE}}")
                print(cierre_encabezado_titulos_ejemplares)
            
        case 6:
            print("\n\t >> Ingresar titulo (con ejemplares) <<\n")
            
            # === VALIDACION DE TITULO ===
            while True:
                nombre_titulo = input("Ingrese el titulo del libro que desea agregar: ").strip()
                if nombre_titulo == "":
                    print("**ERROR** Debe ingresar un valor.")
                    continue  
                elif nombre_titulo in titulos:
                    print("**ERROR** Ese titulo ya existe, por favor ingrese uno nuevo")
                    continue
                break
            
            # === VALIDACION NUMERICA ===
            while True:
                cantidad = input(f"ingrese la cantidad de ejemplares para {nombre_titulo}: ").strip()
                if not cantidad.isdigit():
                    print("**ERROR** Los datos ingresados deben ser solo numericos.")
                    continue
                cantidad = int(cantidad)
                if cantidad < 1 :
                    print(f"**ERROR** El valor ingresado no puede ser 0 o negativo.")
                    continue
                break
            
            '''
            Una que vez que tengo el titulo y la cantidad validados los agrego como nuevos elementos en sus repectivas listas
            '''            
            titulos.append(nombre_titulo)
            ejemplares.append(cantidad)
            
            print(f"\n --- Operacion exitosa, se agrego el titulo: {nombre_titulo} con {cantidad} ejemplares --- \n")
            
        case 7:
            print("\n\t >> Actualizar ejemplares (prestamo/devolucion) <<\n")
            
            # === VALIDACION DE EXISTENCIA DE TITULOS ===
            if not titulos:
                print("**ERROR** No existen titulos ingresados. Para realizar (prestamo/devolucion) deben existir titulos.")
                continue
            
            # === Muestro el listado de las opciones disponbles
            for i, elemento in enumerate(accion):
                print(f"{i+1:>{SPACE_NUM}}. {elemento:<{SPACE_TITULOS}}")
            
            # === VALIDACION NUMERICA ===
            while True:
                opcion = input("Elija una opcion: ").strip()
                if not opcion.isdigit():
                    print("**ERROR** Los datos ingresados deben ser solo numericos.")
                    continue
                opcion = int(opcion)
                if opcion < 1 or opcion > len(accion):
                    print(f"**ERROR** El valor ingresado debe estar entre {1} y {len(accion)}.")
                    continue
                break
            
            # Verifico que haya por lo menos algun ejemeplar disponible para prestamo, caso contrario lo envio al menu principal
            if opcion == 1 and ejemplares.count(0) == len(ejemplares):
                print(f"\n --- NO hay ningun ejemplar disponible para {accion[opcion-1]} ---\n")
                continue
                        
            # === Muestro el listado de titulos existentes
            print(apertura_encabezado_titulo)
            print(titulo_libro)
            print(cierre_encabezado_titulo)
            for i, elemento in enumerate(titulos):
                '''
                si la opcion elegida es prestamo, solo muestro los datos de los ejemplares con valor mayor a 0
                '''
                if (opcion == 1 and ejemplares[i] != 0) or opcion == 2:
                    print(f"| {i+1:>{SPACE_NUM}}. {elemento:<{SPACE_TITULOS}} |")
            print(cierre_encabezado_titulo)
            
            # === ELECCION DE TITULO EXISTENTE ===
            while True:
                titulo_posicion = input(f"Elija el titulo que quiere  para realizar {"un" if opcion == 1 else "una"} {accion[opcion-1]}: ").strip()
                if not titulo_posicion.isdigit():
                    print("**ERROR** Los datos ingresados deben ser solo numericos.")
                    continue
                titulo_posicion = int(titulo_posicion)
                if titulo_posicion < 1 or titulo_posicion > len(titulos):
                    print(f"**ERROR** El valor ingresado debe estar entre {1} y {len(titulos)}.")
                    continue
                
                '''
                Verifico que si la accion es 1(prestamo) y el titulo que desea tenga por los menos 1 ejemplar, sino le pido que elija otro
                '''
                if opcion == 1 and ejemplares[titulo_posicion-1] == 0:
                    print(f"\n -- No se puede realizar {accion[opcion-1]} ya que \"{titulos[titulo_posicion-1]}\" es un titulo existente pero NO tiene ejemplares disponibles. Elija otro titulo --\n")
                    continue
                break
            # si es prestamo reduzco en 1 la cantidad de ejemplares, caso contrario lo aumento en 1
            if opcion == 1: 
                ejemplares[titulo_posicion-1] -= 1               
            else:
                ejemplares[titulo_posicion-1] += 1
            
            print(f"\n --- {accion[opcion-1]} del titulo \"{titulos[titulo_posicion-1]}\" se realizo con exito --- \n")
        case _:
            print("\n\t <<< Fin del programa >>>\n")
            break