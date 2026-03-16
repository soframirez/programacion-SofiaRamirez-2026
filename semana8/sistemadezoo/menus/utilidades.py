def leer_numero(mensaje, tipo=int):
    """
    Solicita una entrada al usuario y garantiza que sea un valor numerico valido.
    
    Esta funcion implementa un bloque try-except para manejar el error 'ValueError',
    lo que asegura que el programa no se detenga (crash) ante entradas invalidas.
    """
    while True:
        # Capturamos la entrada del usuario como texto
        entrada = input(mensaje)
        
        try:
            # Intentamos convertir la entrada a tipo int o float
            valor_validado = tipo(entrada)
            return valor_validado
            
        except ValueError:
            # Si la conversion falla (ej: el usuario escribe "diez" en lugar de 10)
            # mostramos un mensaje de error amigable y el ciclo 'while' se repite.
            if tipo == int:
                print("Error: Se esperaba un numero entero (sin decimales).")
            else:
                print("Error: Se esperaba un numero decimal (use punto para decimales).")
            
            print("Por favor, intente de nuevo.\n")
