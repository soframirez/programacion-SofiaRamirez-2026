# Importa las clases desde la carpeta mundo
from mundo.persona import Personita
from mundo.mascota import Mascota
from mundo.vehiculo import Vehiculo

# Listas vacias para guardar los datos en memoria
lista_personas = []
lista_mascotas = []
lista_vehiculos = []

# Funcion que muestra las opciones en pantalla
def menu():
    print("\n--- SIMULADOR DE MUNDO HAIKYUU ---")
    print("1. Crear persona")
    print("2. Crear mascota")
    print("3. Crear vehiculo")
    print("4. Imprimir personas")
    print("5. Imprimir mascotas")
    print("6. Imprimir vehiculos")
    print("7. Imprimir todas las entidades")
    print("8. Salir")
    return input("Seleccione una opcion: ")

# Inicio del ciclo principal del programa
while True:
    opcion = menu()

    # Logica para registrar una persona
    if opcion == "1": 
        nom = input("Nombre: ")
        ed = input("Edad: ")
        prof = input("Profesion: ")
        # Crea el objeto y lo guarda en la lista
        nueva_p = Personita(nom, ed, prof)
        lista_personas.append(nueva_p)
        print("Persona creada con exito!")
    
    # Logica para registrar una mascota
    elif opcion == "2":
        nomb = input("Nombre: ")
        esp = input("Especie: ")
        raza = input("Raza: ")
        # Crea el objeto y lo guarda en la lista
        nueva_m = Mascota(nomb, esp, raza)
        lista_mascotas.append(nueva_m)
        print("Mascota creada con exito!")

    # Logica para registrar un vehiculo
    elif opcion == "3":
        marc = input("Marca: ")
        mode = input("Modelo: ")
        year = input("Ano de fabricacion: ") # Se usa ano por la instruccion
        # Crea el objeto y lo guarda en la lista
        nuevo_v = Vehiculo(marc, mode, year)
        lista_vehiculos.append(nuevo_v)
        print("Vehiculo creado con exito!")

    # Muestra todas las personas registradas
    elif opcion == "4":
        print("\n--- LISTA DE PERSONAS DE HAIKYUU ---")
        for p in lista_personas:
            print(p) 

    # Muestra todas las mascotas registradas
    elif opcion == "5":
        print("\n--- LISTA DE MASCOTAS DE HAIKYUU ---")
        for m in lista_mascotas:
            print(m)

    # Muestra todos los vehiculos registrados
    elif opcion == "6":
        print("\n--- LISTA DE VEHICULOS DE HAIKYUU ---")
        for v in lista_vehiculos:
            print(v)

    # Une las listas para mostrar todos los objetos creados
    elif opcion == "7":
        print("\n--- TODAS LAS ENTIDADES DE HAIKYUU ---")
        for e in lista_personas + lista_mascotas + lista_vehiculos:
            print(e)

    # Termina la ejecucion del programa
    elif opcion == "8":
        print("Saliendo de la simulacion de Haikyuu...")
        break