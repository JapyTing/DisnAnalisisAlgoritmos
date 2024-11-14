def busqueBin(lista, valor, inicio=0):
    if len(lista) > 2:
        centro = len(lista) // 2
        if valor == lista[centro]:
            return inicio + centro  # Retorna el índice real del valor encontrado
        elif valor > lista[centro]:
            # Llama a la mitad derecha de la lista y ajusta el índice inicial
            return busqueBin(lista[centro + 1:], valor, inicio + centro + 1)
        else:
            # Llama a la mitad izquierda de la lista
            return busqueBin(lista[:centro], valor, inicio)
    elif len(lista) == 2:
        if valor == lista[0]:
            return inicio
        elif valor == lista[1]:
            return inicio + 1
    elif len(lista) == 1:
        if lista[0] == valor:
            return inicio
    return -1  # Si el valor no se encuentra

# Lista ordenada para realizar la búsqueda binaria
lista = [0, 6, 11, 15, 19, 20, 24, 31, 39, 40]
valor_a_buscar = 15
indice = busqueBin(lista, valor_a_buscar)
if indice != -1:
    print(f"El valor {valor_a_buscar} se encuentra en el índice {indice}.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la lista.")
#Complejidad del programa: 0(n)
#Complejidad espacial: 0(1)