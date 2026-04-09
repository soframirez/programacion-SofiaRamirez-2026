import random

def generar_ejercicios(tipo, cantidad):
    #Genera una lista de tuplas con (num1, operacion, num2, resultado)
    ejercicios = []
    simbolos = {
        'suma': '+',
        'resta': '-',
        'multiplicacion': '*',
        'division': '/'
    }
    
    for _ in range(cantidad):
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        
        if tipo == 'suma':
            res = a + b
        elif tipo == 'resta':
            res = a - b
        elif tipo == 'multiplicacion':
            res = a * b
        elif tipo == 'division':
            # Evitar divisiones infinitas, redondeamos a 2 decimales
            res = round(a / b, 2)
            
        ejercicios.append((a, simbolos[tipo], b, res))
    return ejercicios