import json
import csv
import os

class FileConverter:
    # Atributo de clase para almacenar la instancia unica (Patron Singleton)
    _instance = None

    def __new__(cls):
        # Si no existe una instancia previa, se crea una nueva
        if cls._instance is None:
            cls._instance = super(FileConverter, cls).__new__(cls)
        # Se retorna siempre la misma instancia guardada en _instance
        return cls._instance

    def convert(self, fileStr):
        """
        Metodo principal que identifica la extension y redirige al convertidor adecuado.
        """
        # Verifica si el archivo existe fisicamente en el sistema
        if not os.path.exists(fileStr):
            return {"error": f"No se encontro el archivo en: {os.path.abspath(fileStr)}"}

        # Separa el nombre de la extension y la pasa a minusculas
        extension = os.path.splitext(fileStr)[1].lower()
        
        if extension == '.json':
            return self.convertFromJson(fileStr)
        elif extension == '.csv':
            return self.convertFromCSV(fileStr)
        
        return {"error": "Extension no soportada"}

    def convertFromJson(self, jsonFileStr):
        """
        Lee archivos JSON y los transforma en diccionarios de Python.
        """
        try:
            with open(jsonFileStr, 'r', encoding='utf-8') as f:
                # json.load transforma el texto estructurado en un objeto dict
                return json.load(f)
        except Exception as e:
            return {"error": str(e)}

    def convertFromCSV(self, csvFileStr):
        """
        Lee archivos CSV detectando el delimitador automaticamente.
        """
        try:
            with open(csvFileStr, 'r', encoding='utf-8') as f:
                # Analiza una muestra del archivo para identificar si usa coma, punto y coma, etc.
                dialect = csv.Sniffer().sniff(f.read(1024))
                f.seek(0) 
                
                # Crea un lector que mapea cada fila a un diccionario usando los encabezados
                reader = csv.DictReader(f, dialect=dialect)
                return [row for row in reader] # Retorna una lista de diccionarios
        except Exception as e:
            return {"error": str(e)}

# --- BLOQUE DE EJECUCION ---

# Creacion del objeto Singleton (siempre sera el mismo objeto en memoria)
converter = FileConverter()

# 1. Obtiene la ruta absoluta de la carpeta donde se encuentra este codigo
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# 2. Construye la ruta final uniendo la carpeta actual con el nombre del archivo
ruta_final = os.path.join(directorio_actual, "datos.csv")

# 3. Llamada al metodo inteligente de conversion
resultado = converter.convert(ruta_final)

# Muestra el resultado final 
print(resultado)