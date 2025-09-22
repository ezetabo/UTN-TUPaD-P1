# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
tablero = [['-','-','-'],['-','-','-'],['-','-','-']]
turno = 0
largo = len(tablero)
ganador = ''

while True:
    turno += 1
    # === MOSTRAR TABLERO ===
    print(f"\n   *** Turno N°{turno} ***\n")
    print("\t  1 2 3")
    for fila, columnas in enumerate(tablero):
        print(f"\t{fila+1}", end=' ')
        for valor in columnas:
            print(f"{valor}", end=' ')
        print()

    # === TURNO JUGADOR 1 ===
    print("\nJugador N°1, usted es la X")
    fila_x = int(input("elija numero de Fila: ")) - 1
    col_x = int(input("elija numero de columna: ")) - 1
    while tablero[fila_x][col_x] != '-':
        print(f"El casillero f{fila_x+1} c{col_x+1} ya está en uso, elija otro por favor.")
        fila_x = int(input("elija numero de Fila: ")) - 1
        col_x = int(input("elija numero de columna: ")) - 1
    tablero[fila_x][col_x] = 'X'

    # --- Revisar ganador ---
    # Filas
    for i in range(largo):
        tateti = True
        for j in range(1, largo):
            if tablero[i][j] != tablero[i][0] or tablero[i][0] == '-':
                tateti = False
                break
        if tateti:
            ganador = tablero[i][0]
            break

    # Columnas
    if ganador == '':
        for j in range(largo):
            tateti = True
            for i in range(1, largo):
                if tablero[i][j] != tablero[0][j] or tablero[0][j] == '-':
                    tateti = False
                    break
            if tateti:
                ganador = tablero[0][j]
                break

    # Diagonal principal
    if ganador == '':
        tateti = True
        for i in range(1, largo):
            if tablero[i][i] != tablero[0][0] or tablero[0][0] == '-':
                tateti = False
                break
        if tateti:
            ganador = tablero[0][0]

    # Diagonal secundaria
    if ganador == '':
        tateti = True
        for i in range(1, largo):
            if tablero[i][largo-1-i] != tablero[0][largo-1] or tablero[0][largo-1] == '-':
                tateti = False
                break
        if tateti:
            ganador = tablero[0][largo-1]

    # Si gano o llego al limte de turnos romper antes de que juegue el jugador N°2
    if ganador != '' or turno > 4:
        break

    # === MOSTRAR TABLERO ===
    print(f"\n   *** Turno N°{turno} ***\n")
    print("\t  1 2 3")
    for fila, columnas in enumerate(tablero):
        print(f"\t{fila+1}", end=' ')
        for valor in columnas:
            print(f"{valor}", end=' ')
        print()

    # === TURNO JUGADOR 2 ===
    print("\nJugador N°2, usted es la O")
    fila_o = int(input("elija numero de Fila: ")) - 1
    col_o = int(input("elija numero de columna: ")) - 1
    while tablero[fila_o][col_o] != '-':
        print(f"El casillero f{fila_o+1} c{col_o+1} ya está en uso, elija otro por favor.")
        fila_o = int(input("elija numero de Fila: ")) - 1
        col_o = int(input("elija numero de columna: ")) - 1
    tablero[fila_o][col_o] = 'O'

    # --- Revisar ganador ---
    # Filas
    for i in range(largo):
        tateti = True
        for j in range(1, largo):
            if tablero[i][j] != tablero[i][0] or tablero[i][0] == '-':
                tateti = False
                break
        if tateti:
            ganador = tablero[i][0]
            break

    # Columnas
    if ganador == '':
        for j in range(largo):
            tateti = True
            for i in range(1, largo):
                if tablero[i][j] != tablero[0][j] or tablero[0][j] == '-':
                    tateti = False
                    break
            if tateti:
                ganador = tablero[0][j]
                break

    # Diagonal principal
    if ganador == '':
        tateti = True
        for i in range(1, largo):
            if tablero[i][i] != tablero[0][0] or tablero[0][0] == '-':
                tateti = False
                break
        if tateti:
            ganador = tablero[0][0]

    # Diagonal secundaria
    if ganador == '':
        tateti = True
        for i in range(1, largo):
            if tablero[i][largo-1-i] != tablero[0][largo-1] or tablero[0][largo-1] == '-':
                tateti = False
                break
        if tateti:
            ganador = tablero[0][largo-1]

    # Si gano romper
    if ganador != '':
        break

# === RESULTADO FINAL ===
if ganador != '':
    jugador = 1 if ganador == 'X' else 2
    print(f"\n<<<< Felicidades jugador N°{jugador}, ha ganado >>>>")
else:
    print(f"\nEmpate, no hay ganador.")

print(f"\n   *** TABLERO Final ***\n")
print("\t  1 2 3")
for fila, columnas in enumerate(tablero):
    print(f"\t{fila+1}", end=' ')
    for valor in columnas:
        print(f"{valor}", end=' ')
    print()
print(f"\n")


