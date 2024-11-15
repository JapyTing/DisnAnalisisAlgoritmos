import random

# Generación de la lista de artículos con pesos aleatorios
articulos = []
capacidadTotal = 10
for _ in range(capacidadTotal):
    articulos.append(random.randint(1, capacidadTotal))


# Función que organiza los artículos en bolsas
def empaquetar(articulos, capacidad):
    bolsas = []
    espacio_disponible = capacidad
    # Si el artículo cabe en el paquete, resta el espacio disponible
    for articulo in articulos:  
        if articulo <= espacio_disponible:
            espacio_disponible -= articulo
        # Si no cabe, se añade el paquete actual y se inicia uno nuevo
        else: 
            bolsas.append(capacidad - espacio_disponible)
            espacio_disponible = capacidad - articulo
    # Añadir el último paquete a la lista
    bolsas.append(capacidad - espacio_disponible)
    return len(bolsas), bolsas



num_paquetes, detalleBolsas = empaquetar(articulos, capacidadTotal)
print("Se utilizaron", num_paquetes, "paquetes para los artículos.")
print("Espacios ocupados en cada paquete:", detalleBolsas)

#Complejidad de tiempo: O(n)
#Complejiodad de espacio: O(n)