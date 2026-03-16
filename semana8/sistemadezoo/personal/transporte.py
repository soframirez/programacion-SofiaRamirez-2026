class Transporte:
    """
    Clase padre para los medios de transporte internos.
    Gestiona la placa y el modelo de forma encapsulada.
    """
    def __init__(self, placa, modelo):
        #atributos privados
        self.__placa = placa
        self.__modelo = modelo

    @property
    def placa(self):
        #Getter para acceder a la placa
        return self.__placa

    @placa.setter
    def placa(self, valor):
        #Setter para modificar la placa
        self.__placa = valor

    @property
    def modelo(self):
        #Getter para acceder al modelo
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        #Setter para modificar el modelo
        self.__modelo = valor

    def __str__(self):
        #Metodo para representar el transporte como texto
        return f"Placa: {self.__placa} | Modelo: {self.__modelo}"