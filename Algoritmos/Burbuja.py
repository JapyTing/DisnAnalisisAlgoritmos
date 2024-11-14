#Programa que ordena mediante el algoritmo burbuja.
def burbuja (lista):

    #El puntero indicara el ultimo indice que se revisara
    puntero = len(lista) - 1

    for x in range(len(lista)-1):
        
        #Indicamos el primer indice de la lista dada
        y=0 #Indicamos el primer indice de la lista dada


        while y < puntero:

            #Compara el elemetno actual con el que le sigue
            if lista[y] > lista [y+1]:

                #Si el elemento actual es mayor que el siguiente, se intercambiaran
                lista[y], lista[y +1] = lista[y+1], lista[y]

            else:
                #Continua con el siguiente elemento de la lista
                y = y+1

        puntero = puntero - 1

    #Regresamos la lista ordenada
    return lista



lista = [9,4,7,0,1,2,5,6,3,8,]
listaOrdenada = burbuja(lista.copy())

print("Lista desordenada: ", lista)
print("Lista ordenada: ", listaOrdenada)
#Costo de tiempo: O(n^2) (lista desordenada o larga)
#Costo en espacio: 0(1)   (lista un poco mas ordenada)