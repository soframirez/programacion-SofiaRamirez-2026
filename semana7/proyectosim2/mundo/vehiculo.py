from mundo.motor import Motor

# Definicion de la clase para representar un vehiculo
class Vehiculo:
    # Metodo para crear los datos del vehiculo
    def __init__(self, marca, modelo, year, tipo_motor, potencia):
        # Se guardan los datos en los atributos privados de la clase
        self.__marca = marca
        self.__modelo = modelo
        self.__year = year
        # Composicion: El vehiculo CREA su motor internamente
        self.__motor = Motor(tipo_motor, potencia)

    # Getters
    def get_marca(self): return self.__marca
    def get_modelo(self): return self.__modelo
    def get_year(self): return self.__year

    # Setters
    def set_marca(self, m): self.__marca = m
    def set_modelo(self, mod): self.__modelo = mod
    def set_year(self, y): self.__year = y

    def __str__(self):
        return f"Vehiculo: {self.__marca} {self.__modelo} | fabricado en: {self.__motor.get_info()}"

    def __len__(self):
        # Retorna cuando se fabrico el vehiculo
        return int(self.__year)