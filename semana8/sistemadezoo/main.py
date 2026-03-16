"""
SISTEMA DE GESTIÓN DE ZOOLOGICO 
--------------------------------------------------
Este es el punto de entrada principal (EntryPoint) del programa.
Coordina la interacción entre el usuario y los diferentes modulos
de logica de negocio (personal, animales, transporte).
"""

# Importacion de funciones desde el paquete de menus
# Esto mantiene el archivo main.py limpio y enfocado solo en el flujo
from menus.submenus import (
    menu_agregar_empleado, 
    menu_agregar_transporte, 
    menu_agregar_animal
)

def main():
    """
    Funcion principal que inicializa el sistema y mantiene el ciclo de vida
    de la aplicacion mediante un menu interactivo.
    """
    
    # ---------------------------------------------------------
    # LISTAS
    # ---------------------------------------------------------
    empleados = []
    transportes = []
    animales = []

    # ---------------------------------------------------------
    # CICLO PRINCIPAL 
    # ---------------------------------------------------------
    while True:
        print("\n" + "="*50)
        print("     SISTEMA DE ADMINISTRACION: ZOOLOGICO ")
        print("="*50)
        
        # Opciones disponibles
        print("1. Agregar empleado        | 2. Listar empleados")
        print("3. Agregar transporte      | 4. Listar transportes")
        print("5. Agregar animal          | 6. Listar animales")
        print("0. Salir")
        print("-"*50)
        
        opcion = input("\nSeleccione una opcion del menu: ")

        # ---------------------------------------------------------
        # LOGICA DE CONTROL (OPCIONES)
        # ---------------------------------------------------------
        
        #OPCION 1: Registro de Personal
        if opcion == "1":
            #captura de datos en la funcion del paquete menus
            menu_agregar_empleado(empleados)

        #OPCION 2: Listar Personal
        elif opcion == "2":
            print("\n" + "·"*15 + " NÓMINA DE EMPLEADOS " + "·"*15)
            if not empleados:
                print("⚠️ No hay empleados registrados en el sistema.")
            else:
                #El comando print(e) invoca el metodo dunder __str__
                #definido en las clases del paquete personal
                for e in empleados:
                    print(e)

        #OPCION 3: Registro de Vehiculos
        elif opcion == "3":
            menu_agregar_transporte(transportes)

        #OPCION 4: Listar Vehiculos
        elif opcion == "4":
            print("\n" + "·"*15 + " INVENTARIO DE TRANSPORTES " + "·"*15)
            if not transportes:
                print("No hay transportes registrados.")
            else:
                for t in transportes:
                    print(t)

        #OPCION 5: Registro de Fauna
        elif opcion == "5":
            menu_agregar_animal(animales)

        #OPCION 6: Listar Fauna
        elif opcion == "6":
            print("\n" + "·"*15 + " REGISTRO DE ANIMALES " + "·"*15)
            if not animales:
                print("El zoologico aun no tiene animales registrados.")
            else:
                for a in animales:
                    print(a)

        #OPCION 0: Salida del Sistema
        elif opcion == "0":
            print("\n[!] Finalizando sesion...")
            print("Datos procesados correctamente. ¡Hasta pronto!")
            break

        # Manejo de errores para entradas no validas
        else:
            print("\nError: La opcion '" + opcion + "' no es valida.")
            print("Por favor, elija un numero del 0 al 6.")


if __name__ == "__main__":
    main()