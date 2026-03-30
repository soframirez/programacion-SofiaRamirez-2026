from agenda.logica import AgendaManager

def mostrar_menu():
    print("\n" + "="*30)
    print("   SISTEMA DE SHERLOCK HOLMES")
    print("="*30)
    print("1. Cargar agenda (json/csv)")
    print("2. Agregar contacto")
    print("3. Buscar por nombre")
    print("4. Buscar por telefono")
    print("5. Mostrar promedio de edad")
    print("6. Mostrar todos los contactos")
    print("7. Salir")
    return input("Seleccione una opcion: ")

def ejecutar():
   manager = AgendaManager()

   while True:
        opc = mostrar_menu()

        if opc == "1":
            ruta = input("Ingrese el nombre del archivo (ej: datos.csv): ")
            if manager.cargar(ruta):
                print(f"Se cargaron {len(manager.contactos)} contactos con exito.")
            else:
                print("Tu archivo no fue encontrado o se encuentra vacio. Se iniciara una nueva agenda.")
                manager.ruta_actual = ruta

        elif opc == "2":
            nuevo = {
                "nombre": input("Nombre: "),
                "telefono": input("Telefono: "),
                "email": input("Email: "),
                "edad": input("Edad: "),
                "residencia": input("Residencia: ")
            }
            manager.agregar_contacto(**nuevo)
            print("Contacto guardado y archivo actualizado.")

        elif opc == "3":
            nombre = input("Nombre a buscar: ")
            resultados = manager.buscar_por_nombre(nombre)
            for r in resultados: print(r)

        elif opc == "4":
            tel = input("Telefono a buscar: ")
            resultados = manager.buscar_por_telefono(tel)
            for r in resultados: print(r)

        elif opc == "5":
            promedio = manager.calcular_promedio_edad()
            print(f"El promedio de edad es: {promedio:.2f} anhos.")

        elif opc == "6":
            print("\n" + "="*30)
            print("\nLISTA COMPLETA:")
            print("="*30)
            for c in manager.contactos:
                print(f"- {c['nombre']} ({c['telefono']})")

        elif opc == "7":
            print("Saliendo del sistema... ¡Suerte Sherlock!")
            break

if __name__ == "__main__":
    ejecutar()