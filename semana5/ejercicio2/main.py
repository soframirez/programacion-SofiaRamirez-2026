# Importamos el archivo de logica (cesar.py) y le ponemos el apodo 'ces'
import cesar as ces

def menu():
    # Solo muestra las opciones que el usuario puede elegir
    print("\n--- CIFRADO CESAR ---")
    print("1. Encriptar mensaje")
    print("2. Desencriptar mensaje")
    print("3. Salir")

def programa():
    while True:  # Bucle que corre el programa
        menu()
        opcion = input("Elija una opcion: ")

        if opcion == '1':
            # Pedimos el texto y el numero de salto (N)
            msj = input("Texto a encriptar: ")
            n = int(input("Desplazamiento (N): "))
            # Llamamos a la funcion de encriptar y mostramos el resultado
            print(f"Resultado: {ces.encriptar_cesar(msj, n)}")

        elif opcion == '2':
            # Pedimos el texto secreto y el numero de salto que se uso
            msj = input("Texto a desencriptar: ")
            n = int(input("Desplazamiento usado: "))
            # Llamamos a la funcion de desencriptar y mostramos el mensaje original
            print(f"Resultado: {ces.desencriptar_cesar(msj, n)}")

        elif opcion == '3':
            # Salimos del bucle
            print("Saliendo del sistema...")
            break
            
        else:
            print("Opcion no valida, intenta de nuevo.")

# Corre el programa completo
if __name__ == "__main__":
    programa()