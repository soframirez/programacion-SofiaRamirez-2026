import os
import procesador  # Importa el modulo encargado de la logica de datos

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def menu():
    """
    Gestiona la interfaz de usuario por consola y el flujo de control.
    Separa la captura de datos del procesamiento real.
    """
    print("="*30)
    print("   SISTEMA DE ANALISIS    ")
    print("="*30)
    print("1. Procesar archivo CSV")
    print("2. Procesar archivo JSON")
    print("3. Salir")
    
    opcion = input("\nSeleccione una opcion: ")
    
    # Seleccion de la fuente de datos
    if opcion == "1":
        # Une la ruta base con la subcarpeta 'data' y el nombre del archivo
        ruta = os.path.join(BASE_DIR, "data", "datos.csv") 
        datos = procesador.leer_csv(ruta)
    elif opcion == "2":
        ruta = os.path.join(BASE_DIR, "data", "datos.json")
        datos = procesador.leer_json(ruta)
    elif opcion == "3":
        print("Saliendo del sistema...")
        return  
    else:
        print("Error: Opción no válida.")
        return

    # Validacion y Manejo de errores
    # Verifica si se pudo leer
    if datos is None:
        print(f"\n ERROR: No se encontro el archivo en: {ruta}")
        print("Asegurate de que el archivo este dentro de la carpeta 'data'.")
    # Verifica si el archivo tiene datos
    elif len(datos) == 0:
        print("\n El archivo está vacio.")
    else:
        # Calculo y Presentacion de Resultados 
        resultados = procesador.calcular_estadisticas(datos)
        
        if resultados:
            print("\n" + "="*25)
            print("   RESULTADOS FINALES")
            print("="*25)
            # formato de dos decimales para la salida
            print(f"Promedio de Edad:    {resultados['edad']:.2f} años")
            print(f"Promedio de Salario: ${resultados['salario']:.2f}")
            print(f"Promedio de Peso:    {resultados['peso']:.2f} kg")
            print("="*25)


if __name__ == "__main__":
    menu()