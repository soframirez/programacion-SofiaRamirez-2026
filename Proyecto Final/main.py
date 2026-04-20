# Punto de entrada de la Tienda de Videojuegos

import os
from catalogo import Catalogo
from carrito import Carrito
from factura import Factura
from modelos import crear_juego
from validaciones import (
    leer_texto, leer_entero, leer_flotante, leer_esrb, leer_consola, leer_opcion
)

# Obtiene la ruta del directorio donde se encuentra este script
DIR = os.path.dirname(os.path.abspath(__file__))

def elegir_archivo_catalogo() -> str:
    """Permite al usuario elegir que archivo usar como catalogo."""
    print("\n¿Que archivo deseas usar como catalogo?")
    print("  1. catalogo.json")
    print("  2. catalogo.csv")
    # Usa validacion para asegurar que solo entre 1 o 2
    opcion = leer_opcion("Elige (1/2): ", ["1", "2"])
    if opcion == "1":
        return os.path.join(DIR, "catalogo.json")
    return os.path.join(DIR, "catalogo.csv")

# Menu de busqueda con diferentes filtros
def menu_busqueda(catalogo: Catalogo):
    print("\n── BUSCAR ──────────────────────────────")
    print("  1. Por nombre")
    print("  2. Por categoria")
    print("  3. Por consola")
    print("  0. Volver")
    op = leer_opcion("Opcion: ", ["0", "1", "2", "3"])

    if op == "1":
        termino = leer_texto("Nombre a buscar: ")
        resultados = catalogo.buscar_por_nombre(termino)
        catalogo.mostrar_resultados(resultados, f"Busqueda: '{termino}'")

    elif op == "2":
        cat = leer_texto("Categoria: ")
        resultados = catalogo.buscar_por_categoria(cat)
        catalogo.mostrar_resultados(resultados, f"Categoria: '{cat}'")

    elif op == "3":
        consola = leer_consola("Consola (PS5 / XBOX / Nintendo): ")
        resultados = catalogo.buscar_por_consola(consola)
        catalogo.mostrar_resultados(resultados, f"Consola: '{consola}'")

# Funcion para recolectar datos y registrar un nuevo producto
def menu_agregar_juego(catalogo: Catalogo):
    print("\n── AGREGAR VIDEOJUEGO ──────────────────")
    try:
        # Genera el ID automaticamente basandose en el ultimo elemento
        nuevo_id = catalogo.siguiente_id()
        print(f"  ID asignado automaticamente: {nuevo_id}")

        # Captura de datos con validaciones especificas
        nombre    = leer_texto("Nombre: ")
        categoria = leer_texto("Categoria: ")
        precio    = leer_flotante("Precio ($): ", minimo=0.01)
        esrb      = leer_esrb()
        stock     = leer_entero("Stock: ", minimo=0)
        consola   = leer_consola()

        # Empaqueta los datos en un diccionario para el modelo
        data = {
            "id": nuevo_id,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "esrb": esrb,
            "stock": stock,
            "consola": consola
        }
        # Crea la instancia del objeto y lo guarda en el archivo
        juego = crear_juego(data)
        catalogo.agregar(juego) 
        print(f" '{nombre}' agregado al catalogo y archivo actualizado.")

    except ValueError as e:
        print(f"Error: {e}")

# Submenu para gestionar los productos temporales de la compra
def menu_carrito(catalogo: Catalogo, carrito: Carrito):
    while True:
        print("\n── CARRITO ─────────────────────────────")
        print("  1. Agregar juego al carrito")
        print("  2. Eliminar juego del carrito")
        print("  3. Ver carrito")
        print("  0. Volver")
        op = leer_opcion("Opcion: ", ["0", "1", "2", "3"])

        if op == "0":
            break

        elif op == "1":
            try:
                id_juego = leer_entero("ID del juego a agregar: ", minimo=1)
                juego = catalogo.buscar_por_id(id_juego)
                if not juego:
                    print(f"No existe un juego con ID {id_juego}.")
                    continue
                print(f"  → {juego.mostrar_info()}")
                cantidad = leer_entero("Cantidad: ", minimo=1)
                # Intenta añadir al carrito (valida stock internamente)
                carrito.agregar(juego, cantidad)
            except ValueError as e:
                print(f"{e}")

        elif op == "2":
            carrito.mostrar()
            if carrito.esta_vacio:
                continue
            try:
                id_juego = leer_entero("ID del juego a eliminar: ", minimo=1)
                carrito.eliminar(id_juego)
            except ValueError as e:
                print(f"Error: {e}")

        elif op == "3":
            carrito.mostrar()

# Proceso de cierre de venta y exportacion de documentos
def menu_factura(carrito: Carrito):
    if carrito.esta_vacio:
        print("El carrito esta vacio. Agrega juegos antes de generar factura.")
        return

    print("\n── GENERAR FACTURA ─────────────────────")
    try:
        cliente = leer_texto("Nombre del cliente: ")
        factura = Factura(cliente, carrito)
        factura.mostrar_pantalla()

        print("Formato de archivo:")
        print("  1. JSON")
        print("  2. CSV")
        fmt = leer_opcion("Elige (1/2): ", ["1", "2"])
        nombre_archivo = leer_texto("Nombre del archivo (sin extension): ")

        # Exportacion segun el formato elegido
        if fmt == "1":
            factura.guardar_json(nombre_archivo)
        else:
            factura.guardar_csv(nombre_archivo)

        # Si se confirma la compra, se altera el inventario real
        confirmar = leer_opcion("¿Confirmar compra y descontar stock? (S/N): ", ["S", "N"])
        if confirmar == "S":
            for item in carrito.items:
                item.juego.stock -= item.cantidad
            carrito.vaciar()
            print("Compra confirmada. Stock actualizado y carrito vaciado.")
        else:
            print("Informacion: Compra no confirmada. El carrito se mantiene.")

    except ValueError as e:
        print(f"Error: {e}")

# Funcion principal que orquestra la ejecucion
def main():
    print("╔══════════════════════════════════════╗")
    print("║      TIENDA DE VIDEOJUEGOS           ║")
    print("╚══════════════════════════════════════╝")

    # Inicializacion de los objetos principales
    archivo = elegir_archivo_catalogo()
    catalogo = Catalogo(archivo)
    carrito  = Carrito()

    while True:
        print("\n══ MENU PRINCIPAL ══════════════════════")
        print("  1. Ver catalogo completo")
        print("  2. Buscar videojuegos")
        print("  3. Agregar nuevo videojuego")
        print("  4. Gestionar carrito")
        print("  5. Generar factura / Finalizar compra")
        print("  0. Salir")
        print("════════════════════════════════════════")

        op = leer_opcion("Elige una opcion: ", ["0", "1", "2", "3", "4", "5"])

        if op == "0":
            print("¡Hasta luego!")
            break
        elif op == "1":
            catalogo.listar()
        elif op == "2":
            menu_busqueda(catalogo)
        elif op == "3":
            menu_agregar_juego(catalogo)
        elif op == "4":
            menu_carrito(catalogo, carrito)
        elif op == "5":
            menu_factura(carrito)

if __name__ == "__main__":
    main()