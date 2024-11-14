import random

# Bogo Sort
def ordenarBogo(lista):
    def estaOrdenada(lista):
        #Recorre la lista
        for i in range(len(lista) - 1):
        #Verifica elementos mayores que el siguiente
            if lista[i] > lista[i + 1]:
                return False
        return True

    #Mezcla aleatoriamente la lista
    def mezclarLista(lista):
        #Recorre la lista
        for i in range(len(lista)):
            #Indice para intercambiar con el indice actual
            indiceAleatorio = random.randint(0, len(lista) - 1)
            #Intercambio de elementos
            lista[i], lista[indiceAleatorio] = lista[indiceAleatorio], lista[i]

    while not estaOrdenada(lista):
        #Mezcla la lista hasta que este en orden
        mezclarLista(lista)

    return lista

# Código de prueba
lista = [9,4,7,0,1,2,5,6,3,8,]
print("Lista desordenada: ", lista)
listaOrdenada = ordenarBogo(lista)
print("Lista ordenada:", listaOrdenada)


#Complejidad de tiempo: O((n!)*n) en promedio dependera del tamaño de la lista
#Complejidad en espacio: O(1)

