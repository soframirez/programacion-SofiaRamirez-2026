from figura import Figura, Cubo, Paralelepipedo, Cilindro, Esfera, Cono

# Polimorfismo y Principio de Liskov

def imprimir_volumen(figura: Figura):
    """
    Esta funcion aplica el Principio de Sustitucion de Liskov, recibe 
    un objeto de la clase madre (Figura), pero funciona correctamente 
    con cualquier clase hija (Cubo, Esfera, etc.) sin necesidad de saber 
    cual es. 
    """
    resultado = figura.volumen() 
    print(f"\nEl volumen de la figura seleccionada es: {resultado:.2f}")
    # Recortamos el resultado a 2 decimales

# Interfaz y Logica de Control 

def mostrar_menu():
    """Imprime las opciones disponibles para el usuario."""
    print("\n" + "="*25)
    print("   MENÚ DE VOLUMENES")
    print("="*25)
    print("1. Volumen del cubo")
    print("2. Volumen del paralelepipedo")
    print("3. Volumen del cilindro")
    print("4. Volumen de la esfera")
    print("5. Volumen del cono")
    print("6. Salir")

def ejecutar():
    """
    Funcion principal que orquesta la creacion de objetos 
    y la interaccion con el menu.
    """
    # objetos con valores predefinidos segun el requerimiento
    mi_cubo = Cubo(10)
    mi_paralelepipedo = Paralelepipedo(5, 4, 3)
    mi_cilindro = Cilindro(2, 10)
    mi_esfera = Esfera(5)
    mi_cono = Cono(3, 12)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "6":
            print("Cerrando el sistema de cálculo. ¡Hasta luego!")
            break

        # Dependiendo de la opcion, se envia el objeto especifico a la funcion 
        if opcion == "1":
            imprimir_volumen(mi_cubo)
        elif opcion == "2":
            imprimir_volumen(mi_paralelepipedo)
        elif opcion == "3":
            imprimir_volumen(mi_cilindro)
        elif opcion == "4":
            imprimir_volumen(mi_esfera)
        elif opcion == "5":
            imprimir_volumen(mi_cono)
        else:
            print("Error: Opcion no valida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    ejecutar()