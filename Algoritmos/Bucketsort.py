def bucketSort(lista):
    # Crear una lista de buckets vacíos y a su vez
    # creamos 10 buckets, uno para cada posible valor en el rango [0, 9]
    bucket = [[] for _ in range(10)]  

    # Colocamos cada elemento en su bucket correspondiente
    for i in lista:
        #Indice
        indice = i  
        bucket[indice].append(i)
    
    # Ordena cada bucket en uno diferente de manera individual
    for j in range(len(bucket)):
        bucket[j] = sorted(bucket[j])

    # Combina los elementos de los buckets en la lista original
    indiceOrdenado = 0
    for buck in bucket:
        for i in buck:
            lista[indiceOrdenado] = i
            indiceOrdenado += 1

    return lista

# Ejemplo de uso
lista = [9, 4, 7, 0, 1, 2, 5, 6, 3, 8]
print("Lista desordenada:", lista)
listaOrdenada = bucketSort(lista)
print("Lista ordenada:", listaOrdenada)

#Complejidad de tiempo: O(n+k+nlog n/k) en caso promedio
#Complejidad en espacio: O(n + k)