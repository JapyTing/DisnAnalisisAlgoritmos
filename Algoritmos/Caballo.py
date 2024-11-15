#Backtracking
# Verifica si una posición en el tablero es válida:
def posicionEsValida(fila, columna, tablero):
    return (0 <= fila < tamañoTablero and 
            0 <= columna < tamañoTablero and 
            tablero[fila][columna] == -1)

# Intenta recorrer el tablero con un "tour" del caballo
def intentarTour(fila, columna, paso, tablero):
    # Caso base: si se han cubierto todas las casillas, el tour es completo
    if paso == tamañoTablero * tamañoTablero:
        return True

    # Explora todos los movimientos 
    for indice in range(8):
        siguienteFila = fila + saltosX[indice]
        siguienteColumna = columna + saltosY[indice]
        # Si el movimiento es válido, marca la posición y continúa con el siguiente paso
        if posicionEsValida(siguienteFila, siguienteColumna, tablero):
            tablero[siguienteFila][siguienteColumna] = paso
            if intentarTour(siguienteFila, siguienteColumna, paso + 1, tablero):
                # Si encuentra una solución, termina el proceso
                # Si no hay solución, deshace el movimiento (backtracking)
                return True  
            tablero[siguienteFila][siguienteColumna] = -1
    return False

# Comienza el caballo desde la esquina superior izquierda
def iniciarTourCaballo():

    # Tablero inicializado con -1 (casillas no visitadas)
    tablero = [[-1 for _ in range(tamañoTablero)] for _ in range(tamañoTablero)]
    tablero[0][0] = 0 

    #Realiza el tour y muestra el resultado
    if intentarTour(0, 0, 1, tablero):
        for fila in tablero:
            print(fila) 

# Tamaño del tablero de ajedrez
tamañoTablero = 8  

# Movimientos posibles del caballo en ajedrez
saltosX = [2, 1, -1, -2, -2, -1, 1, 2]
saltosY = [1, 2, 2, 1, -1, -2, -2, -1]
iniciarTourCaballo()

#Complejidad en tiempo: O(8^N^2)
#Complejidad en espacio: O(N^2)
