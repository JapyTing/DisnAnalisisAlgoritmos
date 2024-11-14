def mochila(capacidad, elementos, n):
    #Tabla de (n+1) filas y (capacidad+1) columnas, inicializada con ceros.
    #tabla[i][w] almacenará el valor máximo que se puede obtener
    #usando los primeros  elementos y una capacidad máxima .
    # i = elementos, w = capacidad
    tabla = [[0 for x in range(capacidad + 1)] for y in range(n + 1)]

    # Recorremos cada elemento desde 1 hasta n (inclusive).
    for i in range(1, n + 1):
        #Peso y el valor del elemento i-ésimo (elementos está indexado desde 0).
        peso = elementos[i - 1][0]
        valor = elementos[i - 1][1]
        
        # Recorremos todas las capacidades posibles
        for w in range(capacidad + 1):
            if peso <= w:

                #Evaluamos dos opciones: incluir o excluir el elemento.
                #- Incluir el elemento: sumamos su valor al mejor valor con el peso restante (w - peso).
                #- Excluir el elemento: mantenemos el valor máximo sin incluirlo.
                tabla[i][w] = max(valor + tabla[i - 1][w - peso], tabla[i - 1][w])
            else:
                #Si el peso del elemento es mayor que la capacidad actual (w),
                #se excluye el elemento y conservamos el valor máximo previo.
                tabla[i][w] = tabla[i - 1][w]

    #El valor máximo que se puede obtener con n elementos y la capacidad dada
    #está en la última celda de la tabla,
    return tabla[n][capacidad]

#Lista de elementos, donde cada elemento es una lista [peso, valor].
elementos = [[1, 1], [3, 4], [4, 5], [5, 7]]
#Capacidad máxima de la mochila.
capacidad = 9
#Número de elementos en la lista.
n = len(elementos)

resultado = mochila(capacidad, elementos, n)
print(f"El valor máximo que se puede obtener es: {resultado}")\
#Complejidad en tiempo: O(n x capacidad)
#Complejidad en espacio: O(n x capacidad)