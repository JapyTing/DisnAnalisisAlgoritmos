def mergeSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        # Aplicando la división de la lista completa
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        
        # Se llama recursivamente para cada mitad
        izquierda = mergeSort(izquierda)
        derecha = mergeSort(derecha)
        
        # Inicializando la lista resultado
        resultado = []
        
        # Índices para recorrer sublistas izquierda y derecha
        i = 0
        d = 0
        
        # Compara y mezcla elementos de izquierda y derecha en resultado, de forma ordenada
        while i < len(izquierda) and d < len(derecha):
            if izquierda[i] < derecha[d]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[d])
                d += 1

        # Copia cualquier elemento restante de izquierda en resultado
        while i < len(izquierda):
            resultado.append(izquierda[i])
            i += 1

        # Copia cualquier elemento restante de derecha en resultado
        while d < len(derecha):
            resultado.append(derecha[d])
            d += 1

    return resultado

lista = [20, 39, 15, 6, 0, 11, 24, 40, 19, 31]
listaOrdenada = mergeSort(lista.copy())
print("Lista desordenada: ", lista)
print("Lista ordenada: ", listaOrdenada)

#Costo de tiempo: O(nlogn) En diversos caso, puede irle bien o mal
#Costo en espacio: O(n)