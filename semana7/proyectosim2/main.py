# Importa las clases desde la carpeta mundo
from mundo.persona import Personita
from mundo.mascota import Mascota
from mundo.vehiculo import Vehiculo

# Listas vacias para guardar los datos en memoria
lista_p = []
lista_m = []
lista_v = []

# Funcion que muestra las opciones en pantalla
def menu():
    print("\n--- SIMULADOR DE MUNDO HAIKYUU ---")
    print("1. Crear persona")
    print("2. Crear mascota")
    print("3. Crear vehiculo (con motor)")
    print("4. Imprimir todo")
    print("8. Salir")
    return input("Seleccione una opcion: ")

# Inicio del ciclo principal del programa
while True:
    op = menu()
    
    # Opcion 1: Registro de personas con asociacion
    if op == "1":
        n = input("Nombre: ")
        e = input("Edad: ")
        p = input("Profesion: ")
        per = Personita(n, e, p)
        
        # ASOCIACION: Si ya existen mascotas, asociamos la mas reciente
        if lista_m:
            per.set_mascota(lista_m[-1])
            print(f"Se asocio la mascota {lista_m[-1].get_nombre()} a esta persona.")
        
        lista_p.append(per)
        print("Persona creada con exito!")

    # Opcion 2: Registro de mascotas
    elif op == "2":
        nomb = input("Nombre de la mascota: ")
        esp = input("Especie: ")
        raza = input("Raza: ")
        masc = Mascota(nomb, esp, raza)
        lista_m.append(masc)
        print("Mascota registrada!")

    # Opcion 3: Registro de vehiculos con composicion
    elif op == "3":
        m = input("Marca: ")
        mod = input("Modelo: ")
        y = input("Anio: ")
        # Datos para el Motor (Composicion)
        t_mot = input("Tipo de motor (V8, Turbo, Electrico): ")
        pot = input("Caballos de fuerza (CV): ")
        
        # El Vehiculo crea su propio Motor internamente
        veh = Vehiculo(m, mod, y, t_mot, pot)
        lista_v.append(veh)
        print("Vehiculo fabricado con su motor!")

    # Opcion 4: Mostrar todo usando __str__ y __len__
    elif op == "4":
        print("\n--- REPORTE GENERAL DEL MUNDO ---")
        # Sumamos las listas para recorrer todos los objetos
        for obj in lista_p + lista_m + lista_v:
            # Imprime el objeto (__str__) y su longitud (__len__)
            print(f"{obj} | (Dato len: {len(obj)})")

    # Opcion 8: Salida del sistema
    elif op == "8":
        print("Saliendo de la simulacion de Haikyuu... ¡Adios!")
        break

    else:
        print("Opcion no valida")
