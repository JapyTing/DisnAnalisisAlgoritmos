def revFilaColumna(fila, columna, numReinas):
    #Verifica si hay una reina en la misma fila o columna.
    for i in range(numReinas):
        if tablero[fila][i] == 'R' or tablero[i][columna] == 'R':
            return False
    return True

def revDiagonalPrincipal(fila, columna, numReinas):
    #Verifica si hay una reina en la diagonal principal.
    filaActual, columnaActual = fila, columna
    while filaActual >= 0 and columnaActual >= 0:
        if tablero[filaActual][columnaActual] == 'R':
            return False
        filaActual -= 1
        columnaActual -= 1

    filaActual, columnaActual = fila, columna
    while filaActual < numReinas and columnaActual < numReinas:
        if tablero[filaActual][columnaActual] == 'R':
            return False
        filaActual += 1
        columnaActual += 1

    return True


def revisar_diagonal_secundaria(fila, columna, numReinas):
    #Verifica si hay una reina en la diagonal secundaria.
    filaActual, columnaActual = fila, columna
    while filaActual >= 0 and columnaActual < numReinas:
        if tablero[filaActual][columnaActual] == 'R':
            return False
        filaActual -= 1
        columnaActual += 1

    filaActual, columnaActual = fila, columna
    while filaActual < numReinas and columnaActual >= 0:
        if tablero[filaActual][columnaActual] == 'R':
            return False
        filaActual += 1
        columnaActual -= 1

    return True


def casillaSegura(fila, columna, numReinas):
    #Verifica si la casilla (fila, columna) está libre de ataques.
    return (revFilaColumna(fila, columna, numReinas) and
            revDiagonalPrincipal(fila, columna, numReinas) and
            revisar_diagonal_secundaria(fila, columna, numReinas))


def colocar_reinas(numReinas, reinasPorColocar):
    #Coloca el número requerido de reinas en el tablero.
    if reinasPorColocar == 0:
        return True

    for fila in range(numReinas):
        for columna in range(numReinas):
            if casillaSegura(fila, columna, numReinas):
                tablero[fila][columna] = 'R'
                if colocar_reinas(numReinas, reinasPorColocar - 1):
                    return True
                tablero[fila][columna] = '_'
    return False

# Número fijo de reinas: 8
numReinas = 8
tablero = [['_'] * numReinas for _ in range(numReinas)]
# Coloca las reinas y muestra el tablero
colocar_reinas(numReinas, numReinas)
for fila in tablero:
    print(' '.join(fila))

#Complejidad en tiempo: O(N!)
#Complejidad en espacio: O(N^2)

