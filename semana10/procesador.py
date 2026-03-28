import csv
import json
import os

# Extraccion de datos

def leer_csv(ruta):
    """
    Lee un archivo CSV y lo convierte en una lista de diccionarios.
    Cada fila se transforma en un objeto clave
    """
    datos = []
    # Verificacion de existencia para evitar errores
    if not os.path.exists(ruta):
        return None
    
    # Abrimos con encoding 'utf-8' para evitar errores por caracteres especiales
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        # DictReader mapea 'edad', 'salario', etc.
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

def leer_json(ruta):
    """
    Carga un archivo JSON y lo convierte en estructuras de Python
    """
    if not os.path.exists(ruta):
        return None
        
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        # json.load procesa el archivo completo de una sola vez
        return json.load(archivo)

# Transformacion y Analisis

def calcular_estadisticas(lista_personas):
    """
    Calcula promedios para edad, salario y peso.
    Manejo de excepciones
    """
    if not lista_personas:
        return None
    
    suma_edad = 0
    suma_salario = 0
    suma_peso = 0
    total = len(lista_personas)

    try:
        # Itera sobre la coleccion de datos
        for p in lista_personas:
            # Los CSV siempre leen datos como Strings, por eso el float()
            suma_edad += float(p['edad'])
            suma_salario += float(p['salario'])
            suma_peso += float(p['peso'])

        # Retorna los promedios calculados
        return {
            "edad": suma_edad / total,
            "salario": suma_salario / total,
            "peso": suma_peso / total
        }
        
    except KeyError as e:
        # Se activa si el archivo no tiene las columnas esperadas
        print(f"Error: No se encontro la columna {e} en el archivo.")
        return None
    except ValueError:
        # Se activa si una celda contiene texto donde debería haber un numero
        print("Error: Uno de los datos no es un numero valido (ej. letras en el peso).")
        return None