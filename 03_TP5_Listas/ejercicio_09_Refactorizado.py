# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
tablero = [['-','-','-'],['-','-','-'],['-','-','-']]
turno = 0
largo = len(tablero)
ganador = ''
jugador = 'X'
jugada = 0
while True:    
    # === MOSTRAR TABLERO ===
    print(f"\n   *** Turno N°{turno+1} ***\n")
    print("\t  1 2 3")
    for fila, columnas in enumerate(tablero):
        print(f"\t{fila+1}", end=' ')
        for valor in columnas:
            print(f"{valor}", end=' ')
        print()

    # === TURNO JUGADOR ===
    print(f"\nJugador {jugador}")
    fila = int(input("elija numero de Fila: ")) - 1
    col = int(input("elija numero de columna: ")) - 1   
    
    if fila < 0 or fila > 2 or col < 0 or col > 2:
        print(f"El casillero f{fila +1} c{col +1} no es un casillero, elija otro por favor.")       
        continue #No soy partidario de usar continue, prefiero validar con while, pero en este caso sirve.
    if tablero[fila][col] != '-':
        print(f"El casillero f{fila +1} c{col +1} ya está en uso, elija otro por favor.")       
        continue
    tablero[fila][col] = jugador

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

    #Cambiar letra de jugador
    jugador = 'O' if jugador == 'X' else 'X'
    #Contar jugadas
    jugada += 1
    # Si gano o llego al limte de jugadas romper
    if ganador != '' or jugada > 9:
        break

# === RESULTADO FINAL ===
if ganador != '':    
    print(f"\n<<<< Felicidades jugador {jugador}, ha ganado >>>>")
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


