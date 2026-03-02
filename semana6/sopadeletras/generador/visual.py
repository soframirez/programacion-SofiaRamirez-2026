def imprimir_sopa(matriz, mapa_colores=None):
    #Imprime la matriz en consola con colores.
    
    RESET = "\033[0m" # Vuelve al color normal

    print("\n" + " =" * 18)
    for f in range(len(matriz)):
        linea = ""
        for c in range(len(matriz)):
            letra = matriz[f][c]
            
            # Si la coordenada tiene un color asignado en el mapa
            if mapa_colores and (f, c) in mapa_colores:
                color = mapa_colores[(f, c)]
                linea += f"{color}{letra}{RESET} "
            else:
                linea += f"{letra} "
        print(linea)
    print(" =" * 18)