# Definicion de la clase para representar un vehiculo
class Vehiculo:
    # Metodo para crear los datos del vehiculo
    def __init__(self, marca, modelo, year):
        # Se guardan los datos en los atributos de la clase
        self.marca = marca
        self.modelo = modelo
        self.year = year

    # Metodo para mostrar la informacion del vehiculo como texto
    def __str__(self):
        # Retorna la marca, modelo y ano de fabricacion
        return f"Vehiculo: {self.marca} - {self.modelo}: {self.year}"