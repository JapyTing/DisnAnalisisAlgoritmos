#Programa que ordena una lista mediante QuickSort
def quickSort (lista):

    #Verificamos que la lista sea larga
    if len(lista) <= 1:
        return lista
    #Se elige el ultimo elemento de la lista como pivote, posterior se crea dos listas vacias, una de lado izquierdo
    #Y otra del lado derecho, estas tendran elementos menores y mayores que el pivote asignado.
    else:
        pivote = lista[-1]
        divIzquirda = []
        divDerecha = []

    #Recorre todos menos el pivote
    for x in lista[:-1]:

        #En n iteracion se compara cada elemento x con el pivote, dependiendo  si es mayor o menor se a;ade a derecha (mayor) o izquierda (menor)
        if x > pivote:
            divDerecha.append(x)

        else:
            divIzquirda.append(x)
    resultado = quickSort(divIzquirda) + [pivote] + quickSort(divDerecha)
    return resultado  

lista = [20,39,15,6,0,11,24,40,19,31]
listaOrdenada = quickSort(lista.copy())
print("Lista desordenada: ", lista)
print("Lista ordenada: ", listaOrdenada)

#Complejidad de tiempo: O(nlogn) en promedio
#Complejidad en espacio: O(logn)
