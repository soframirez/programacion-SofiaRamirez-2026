from menus.utilidades import leer_numero
from personal.tipos_empleados import Administrador, Guardian, Conserje, Veterinario
from personal.tipos_transporte import Bicicleta, Cuadraciclo, Patineta
from animales.especies import Serpiente, Leon, Aguila, Tiburon, Rana

def menu_agregar_animal(lista):
    """Maneja la logica de creacion de objetos de tipo Animal y sus subclases."""
    print("\n--- AGREGAR ANIMAL ---")
    print("5.1 Agregar Reptil (Serpiente)\n5.2 Agregar Mamifero (Leon)")
    print("5.3 Agregar Ave (Aguila)\n5.4 Agregar Pez (Tiburon)")
    print("5.5 Agregar Anfibio (Rana)")
    
    op = input("Seleccione sub-opcion: ")
    nom = input("Nombre individual: ")
    edad = leer_numero("Edad: ", int) # Validación de entero
    
    # Instanciación basada en la opción del submenú
    if op == "5.1":
        esc = input("Tipo de escamas: ")
        lon = leer_numero("Longitud (m): ", float) # Validación de float
        lista.append(Serpiente(nom, edad, esc, lon))
    elif op == "5.2":
        pel = input("Tipo de pelaje: ")
        r = input("Potencia rugido (dB): ")
        lista.append(Leon(nom, edad, pel, r))
    elif op == "5.3":
        env = leer_numero("Longitud de las alas (m): ", float)
        vuelo = input("Tipo de vuelo: ")
        lista.append(Aguila(nom, edad, env, vuelo))
    elif op == "5.4":
        agua = input("Tipo de agua (Salada/Dulce): ")
        d = leer_numero("Numero de dientes: ", int)
        lista.append(Tiburon(nom, edad, agua, d))
    elif op == "5.5":
        piel = input("Tipo de piel: ")
        col = input("Color: ")
        lista.append(Rana(nom, edad, piel, col))
    
    print("¡Animal registrado correctamente!")

def menu_agregar_empleado(lista_empleados):
    """Maneja la logica de creacion de objetos de tipo Empleado y sus subclases."""
    print("\n--- AGREGAR EMPLEADO ---")
    print("1.1 Administrador\n1.2 Guardian\n1.3 Conserje\n1.4 Veterinario")
    sub_op = input("Seleccione sub-opcion: ")

    nom = input("Nombre completo: ")
    id_e = input("ID de empleado: ")

    # Cada bloque crea una instancia específica pasando los argumentos al constructor (__init__)
    if sub_op == "1.1":
        depto = input("Departamento: ")
        lista_empleados.append(Administrador(nom, id_e, depto))
    elif sub_op == "1.2":
        turno = input("Turno (Dia/Tarde/Noche): ")
        lista_empleados.append(Guardian(nom, id_e, turno))
    elif sub_op == "1.3":
        area = input("Area asignada: ")
        lista_empleados.append(Conserje(nom, id_e, area))
    elif sub_op == "1.4":
        esp = input("Especialidad medica: ")
        lista_empleados.append(Veterinario(nom, id_e, esp))
    else:
        print("Opción no valida.")
        return
    print(f"¡{nom} registrado con exito!")

def menu_agregar_transporte(lista_transportes):
    """Maneja la logica de creacion de objetos de tipo Transporte y sus subclases."""
    print("\n--- AGREGAR MEDIO DE TRANSPORTE ---")
    print("3.1 Bicicleta\n3.2 Cuadraciclo\n3.3 Patineta")
    sub_op = input("Seleccione sub-opcion: ")

    placa = input("Numero de placa: ")
    modelo = input("Modelo: ")

    if sub_op == "3.1":
        freno = input("Tipo de freno: ")
        lista_transportes.append(Bicicleta(placa, modelo, freno))
    elif sub_op == "3.2":
        cil = leer_numero("Cilindrada (cc): ", int)
        lista_transportes.append(Cuadraciclo(placa, modelo, cil))
    elif sub_op == "3.3":
        elec = input("¿Es electrica? (si/no): ").lower() == 'si'
        lista_transportes.append(Patineta(placa, modelo, elec))
    else:
        print("Opción no valida.")
        return
    print(f"Transporte [{placa}] registrado con exito!")