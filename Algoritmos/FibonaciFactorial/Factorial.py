#Programa que calcula el factorial de un numero dado
def fact(n):

    #Por definicion el factorial de 0 es 1
    if n == 0:
        return 1
    else:
        #Sacamos el factorial multiplicando el numero por el mismo numero -1 
        #hasta que el numero dado llegue a 0
        return n*fact(n-1)



num = int(input("Ingrese un numero para calcular el factoria: "))
numFact = print(fact(num))
#Costo de tiempo = 0(n) contando la recursividad.
#Costo de memmoria = 0(n) contando el n de pilas
