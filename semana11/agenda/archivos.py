import csv
import json
import os

class Procesadordatos:
    @staticmethod
    def leer(ruta):
        """
        Fusiona leer_csv y leer_json. 
        Detecta el formato por la extension y maneja errores.
        """
        if not os.path.exists(ruta):
            print(f"Error: El archivo {ruta} no existe.")
            return None

        # Obtenemos la extension para decidir que logica usar
        _, extension = os.path.splitext(ruta.lower())

        try:
            with open(ruta, mode='r', encoding='utf-8') as archivo:
                if extension == '.csv':
                    return list(csv.DictReader(archivo))
                elif extension == '.json':
                    return json.load(archivo)
                else:
                    print("Error: Formato no soportado.")
                    return None
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None

    @staticmethod
    def guardar(ruta, datos):
        """Escribe los datos segun el archivo."""
        _, extension = os.path.splitext(ruta.lower())
        
        try:
            with open(ruta, mode='w', encoding='utf-8', newline='') as archivo:
                if extension == '.json':
                    json.dump(datos, archivo, indent=4, ensure_ascii=False)
                elif extension == '.csv':
                    if not datos: return
                    escritor = csv.DictWriter(archivo, fieldnames=datos[0].keys())
                    escritor.writeheader()
                    escritor.writerows(datos)
        except Exception as e:
            print(f"Error al guardar: {e}")