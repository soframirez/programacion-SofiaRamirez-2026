from generador.logic import matriz, palabra_color, rellenar_vacias
from generador.visual import imprimir_sopa

def ejecutar_programa():
    # Variables iniciales
    palabras_ingresadas = []
    mapa_colores_respuestas = {} # Diccionario {(fila, col): "codigo_color"}
    tamano_matriz = 15
    max_palabras = 15
    
    # Crea la matriz base vacia
    sopa = matriz(tamano_matriz)

    print("--- GENERADOR DE SOPA DE LETRAS - DR. HOUSE ---")
    print(f"Ingrese hasta {max_palabras} palabras")
    
    # 1. Fase de ingreso de palabras
    while len(palabras_ingresadas) < max_palabras:
        print(f"\nPalabras actuales: {len(palabras_ingresadas)}/{max_palabras}")
        nueva = input("Ingrese una palabra (o escriba 'fin' para generar): ").strip()
        
        # Opcion para terminar antes
        if nueva.lower() == 'fin':
            if len(palabras_ingresadas) == 0:
                print("Debe ingresar al menos una palabra.")
                continue
            break
            
        # Validacion de longitud
        if len(nueva) > tamano_matriz:
            print(f"Error: La palabra '{nueva}' es muy larga para el tablero.")
            continue
        
        if len(nueva) < 2:
            print("Error: Ingrese palabras de al menos 2 letras.")
            continue

        # Coloca la palabra con un color unico
        # Enviamos len(palabras_ingresadas) como indice para variar el color
        exito = palabra_color(sopa, nueva, mapa_colores_respuestas, len(palabras_ingresadas))
        
        if exito:
            palabras_ingresadas.append(nueva.upper())
            print(f"¡Palabra '{nueva.upper()}' agregada con exito!")
        else:
            print("No se pudo colocar la palabra (tablero muy lleno). Intente con otra.")

    # 2. Rellenar los espacios vacios con letras al azar antes de mostrar
    rellenar_vacias(sopa)

    # 3. Menu de visualizacion y resolucion
    while True:
        print("\n--- MENU DE LA SOPA DE LETRAS ---")
        print("1. Ver sopa de letras")
        print("2. Ver lista de palabras a buscar")
        print("3. Resolver sopa (Mostrar colores)")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            #Imprime la sopa de letras
            print("\nSOPA DE LETRAS PERSONALIZADA:")
            imprimir_sopa(sopa)
            
        elif opcion == "2":
            # Ver la lista de palabras
            print("\nPALABRAS OCULTAS:")
            if not palabras_ingresadas:
                print("(No hay palabras registradas)")
            else:
                for p in palabras_ingresadas:
                    print(f"- {p}")
            
        elif opcion == "3":
            # Resolver la sopa
            print("\nSOLUCION (CADA PALABRA TIENE UN COLOR):")
            imprimir_sopa(sopa, mapa_colores_respuestas)
                
        elif opcion == "4":
            #Salir del sistema
            print("Saliendo del sistema... ¡Suerte!")
            break
        else:
            print("Opcion no valida, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_programa()