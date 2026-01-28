def gen_fibonacci():
    print("--------Generador de Secuencia Fibonacci Sofi--------")
    
    try:
        n= int(input(f'Cuantos numeros de la secuencia de Fibonacci quieres ver? '))

        if n <= 0:
            print(f'Error - Por favor ingresa un numero mayor a 0.')
            return
    except ValueError:
        print(f'Error - Por favor ingresa un numero entero')
        return
    a=0
    b=1

    print(f'\nLos primeros {n} números de la secuencia son:')

    for i in range(n):
        print(a, end=" ")

        a, b = b, a+b

    print(f'\n')

if __name__ == "__main__":
    gen_fibonacci()     