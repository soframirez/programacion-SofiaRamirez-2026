from generador.operaciones import generar_ejercicios
from generador.archivos import guardar_practica, guardar_respuestas

def menu():
    print("--- Sistema de Practicas ---")
    try:
        s = int(input("¿Cuantas sumas desea?: "))
        r = int(input("¿Cuantas restas desea?: "))
        m = int(input("¿Cuantas multiplicaciones desea?: "))
        d = int(input("¿Cuantas divisiones desea?: "))
        
        todos_los_ejercicios = []
        
        # Generar cada grupo
        todos_los_ejercicios.extend(generar_ejercicios('suma', s))
        todos_los_ejercicios.extend(generar_ejercicios('resta', r))
        todos_los_ejercicios.extend(generar_ejercicios('multiplicacion', m))
        todos_los_ejercicios.extend(generar_ejercicios('division', d))
        
        if not todos_los_ejercicios:
            print("No se generaron ejercicios.")
            return

        # Guardar archivos
        guardar_practica(todos_los_ejercicios)
        guardar_respuestas(todos_los_ejercicios)
        
        print("\n¡Exito! Se han generado 'practica.txt' y 'respuestas.txt'.")
        print("A estudiar se ha dicho.")
        
    except ValueError:
        print("Error: Por favor ingrese solo numeros enteros.")

if __name__ == "__main__":
    menu()