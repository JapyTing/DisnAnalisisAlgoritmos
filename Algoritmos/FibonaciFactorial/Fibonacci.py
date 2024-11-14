#Programa que calcula la secuencia fiboncci de manera recursiva dada un rango
def fibo(n):

    #Si n es  0 o 1 devuelve los dos primeros terminos de fibonacci
    if n == 0 or n ==1:
        return 1
    
    else:
        #Calcula la suma de dos numeros anteriores en la secuencia
        return fibo(n - 1) + fibo(n-2)

numero = int(input("Introduce un rango a calcular: "))

x = 0
#Bucle hasta que el rango introducido se cumpla
while x <= numero:
    print(fibo(x))
    x = x + 1


#Costo en tiempo: O(2^n)  Si hay valores altos
#Costo en espacio: O(n)  promedio