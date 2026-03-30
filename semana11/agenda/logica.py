from .personas import Contacto
from .archivos import Procesadordatos

class AgendaManager:
    def __init__(self):
        # Requisito: Los datos deben mantenerse en memoria
        self.contactos = [] 
        self.ruta_actual = ""

    def cargar(self, ruta):
        """Carga contactos desde un archivo CSV o JSON."""
        datos = Procesadordatos.leer(ruta)
        if datos is not None:
            self.contactos = datos
            self.ruta_actual = ruta
            return True
        return False

    def agregar_contacto(self, nombre, telefono, email, edad, residencia):
        """
        Agrega un contacto en memoria y lo guarda inmediatamente 
        en el archivo sin perder los datos anteriores.
        """
        nuevo = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "edad": edad,
            "residencia": residencia
        }
        # a. Agregar en memoria
        self.contactos.append(nuevo)
        
        # b. Guardar en el archivo (actualización inmediata)
        if self.ruta_actual:
            Procesadordatos.guardar(self.ruta_actual, self.contactos)
        else:
            print("Advertencia: Contacto guardado en memoria, pero no hay archivo cargado.")

    def buscar_por_nombre(self, fragmento):
        """Busqueda parcial por nombre (ej: 'mar' encuentra 'Mario')."""
        return [c for c in self.contactos if fragmento.lower() in c['nombre'].lower()]

    def buscar_por_telefono(self, fragmento):
        """Busqueda parcial por telefono."""
        return [c for c in self.contactos if fragmento in c['telefono']]

    def calcular_promedio_edad(self):
        """Calcula el promedio"""
        if not self.contactos:
            return 0
        
        suma_edad = 0
        try:
            for c in self.contactos:
                # El float() es vital porque el CSV lee texto
                suma_edad += float(c['edad'])
            return suma_edad / len(self.contactos)
        except (ValueError, KeyError):
            return 0

    def obtener_todos(self):
        """Retorna todos los contactos en memoria."""
        return self.contactos