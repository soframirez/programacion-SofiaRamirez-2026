def validacion(texto):
    # Limpieza inicial
    t = "".join(c.lower() for c in texto if c.isalnum())
    
    # Comparación desde los extremos hacia el centro
    inicio = 0
    fin = len(t) - 1
    
    while inicio < fin:
        if t[inicio] != t[fin]:
            return False  # Cuando uno no coincida termina
        inicio += 1
        fin -= 1
    return True

def programa():
    print(f'----------Detector de Palindromos Sofi---------')
    entrada = input(f'Ingresa una palabra o frase: ') #solicitud de cadena
    
    if validacion(entrada):
        print(f' {entrada} -> Si es un palíndromo.')
    else:
        print(f'{entrada} -> No es un palíndromo.')

if __name__ == "__main__":
    programa()