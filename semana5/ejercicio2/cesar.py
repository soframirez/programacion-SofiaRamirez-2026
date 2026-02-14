import string

def encriptar_cesar(texto, n):
    abc = string.ascii_lowercase  # Abecedario en minusculas: 'abcdefghijklmnopqrstuvwxyz'
    resultado = ""

    for letra in texto.lower():
        if letra in abc:
            # Encontramos la posicion actual y sumamos el desplazamiento N
            posicion = abc.find(letra)
            # El % 26 es para que si llega a la 'z', vuelva a empezar desde la 'a'
            nueva_posicion = (posicion + n) % 26
            resultado += abc[nueva_posicion]
        else:
            # Si no es una letra (espacios, numeros), se queda igual
            resultado += letra
    return resultado

def desencriptar_cesar(texto, n):
    # Desencriptar es lo mismo que encriptar, pero restando el desplazamiento
    return encriptar_cesar(texto, -n)