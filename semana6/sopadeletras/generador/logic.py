import random
import string

# Lista de colores para cada palabra que se genere
COLORES = [
    "\033[91m", # Rojo
    "\033[92m", # Verde
    "\033[93m", # Amarillo
    "\033[94m", # Azul
    "\033[95m", # Morado
    "\033[96m", # Turquesa
    "\033[33m", # Naranja
    "\033[35m", # Rosado
]

def matriz(tamano=15):
    """
    Metodo 1: Crea una cuadricula vacia.
    Recibe: El tamano de la matriz (ej. 15).
    Retorna: Una lista de listas llena de espacios.
    """
    return [[" " for _ in range(tamano)] for _ in range(tamano)]

def palabra_color(matriz, palabra, mapa_colores, indice_color):
    """
    Metodo 2: Inserta una palabra en la matriz con un color unico.
    Recibe: La matriz, la palabra, el diccionario de colores y el numero de palabra.
    Retorna: True si pudo colocarla, False si no encontro espacio.
    """
    palabra = palabra.upper()
    tamano = len(matriz)
    colocada = False
    intentos = 0
    
    # Selecciona un color de la lista segun el orden de la palabra
    color_actual = COLORES[indice_color % len(COLORES)]

    while not colocada and intentos < 100:
        direccion = random.choice(["H", "V"]) # Horizontal o Vertical
        
        if direccion == "H":
            fila = random.randint(0, tamano - 1)
            col = random.randint(0, tamano - len(palabra))
            
            # Verificar si el espacio esta libre o tiene la misma letra
            posible = True
            for i in range(len(palabra)):
                if matriz[fila][col + i] != " " and matriz[fila][col + i] != palabra[i]:
                    posible = False
                    break
            
            if posible:
                for i in range(len(palabra)):
                    matriz[fila][col + i] = palabra[i]
                    # Guardamos la coordenada y su color en el diccionario
                    mapa_colores[(fila, col + i)] = color_actual
                colocada = True
        else:
            fila = random.randint(0, tamano - len(palabra))
            col = random.randint(0, tamano - 1)
            
            posible = True
            for i in range(len(palabra)):
                if matriz[fila + i][col] != " " and matriz[fila + i][col] != palabra[i]:
                    posible = False
                    break
            
            if posible:
                for i in range(len(palabra)):
                    matriz[fila + i][col] = palabra[i]
                    # Guardamos la coordenada y su color en el diccionario
                    mapa_colores[(fila + i, col)] = color_actual
                colocada = True
        intentos += 1
    return colocada

def rellenar_vacias(matriz):
    """
    Metodo 3: Llena los huecos sobrantes con letras al azar.
    Recibe: La matriz con las palabras ya colocadas.
    Retorna: La matriz completa lista para mostrarse.
    """
    for f in range(len(matriz)):
        for c in range(len(matriz)):
            if matriz[f][c] == " ":
                matriz[f][c] = random.choice(string.ascii_uppercase)