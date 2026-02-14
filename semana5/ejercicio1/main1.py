# Traemos las fórmulas matemáticas del otro archivo (volumenes.py)
import volumenes as vol 

def menu():
    # Solo imprime las opciones en pantalla
    print("\n--- CALCULADORA DE VOLUMEN SOFI ---")
    print("1. Cubo\n2. Paralelepípedo\n3. Cilindro\n4. Esfera\n5. Cono\n6. Salir")

def programa():
    while True: # Repite el menú hasta que el usuario decida salir
        menu()
        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == '1':
            l = float(input("Lado del cubo: "))
            # Usamos la función del módulo 'vol'
            resultado = vol.calcular_cubo(l)
            print(f"Volumen: {resultado:.2f}")

        elif opcion == '2':
            l = float(input("Largo: "))
            b = float(input("Ancho: "))
            h = float(input("Altura: "))
            resultado = vol.calcular_paralelepipedo(l, b, h)
            print(f"Volumen: {resultado:.2f}")

        elif opcion == '3':
            r = float(input("Radio: "))
            h = float(input("Altura: "))
            resultado = vol.calcular_cilindro(r, h)
            print(f"Volumen: {resultado:.2f}")

        elif opcion == '4':
            r = float(input("Radio de la esfera: "))
            resultado = vol.calcular_esfera(r)
            print(f"Volumen: {resultado:.2f}")

        elif opcion == '5':
            r = float(input("Radio del cono: "))
            h = float(input("Altura: "))
            resultado = vol.calcular_cono(r, h)
            print(f"Volumen: {resultado:.2f}")

        elif opcion == '6':
            print("¡Adiós!")
            break # Rompe el bucle y cierra el programa
        
        else:
            print("Opción no válida, intenta de nuevo.")

# Inicia el programa principal
if __name__ == "__main__":
    programa()