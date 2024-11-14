def subcadena_comun_mas_larga(cadena1, cadena2):
    longitud_maxima = 0
    subcadena_larga = ""

    # Se lee ambas cadenas para encontrar coincidencias
    for i in range(len(cadena1)):
        for j in range(len(cadena2)):
            # Contador común
            k = 0
            # Asegura que ambas posiciones de la cadena coincidan
            while (i + k) < len(cadena1) and (j + k) < len(cadena2) and cadena1[i + k] == cadena2[j + k]:
                k += 1
            if k > longitud_maxima:
                # Actualiza la longitud máxima
                longitud_maxima = k
                subcadena_larga = cadena1[i:i + k]

    return subcadena_larga

# Ejemplo de uso
cadena1 = "aabcakcac"
cadena2 = "aabcabacba"
print("La subcadena común más larga es:", subcadena_comun_mas_larga(cadena1, cadena2))
