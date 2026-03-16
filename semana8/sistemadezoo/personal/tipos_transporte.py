# Importa la clase padre Transporte
from .transporte import Transporte

class Bicicleta(Transporte):
    """
    Representa una bicicleta de uso interno.
    Hereda de Transporte: placa y modelo.
    """
    def __init__(self, placa, modelo, tipo_freno):
        super().__init__(placa, modelo)
        self.__tipo_freno = tipo_freno

    @property
    def tipo_freno(self): return self.__tipo_freno
    
    @tipo_freno.setter
    def tipo_freno(self, v): self.__tipo_freno = v

    def __str__(self):
        #Muestra la placa y modelo heredados, mas el tipo de freno
        return super().__str__() + f" | Tipo: Bicicleta | Freno: {self.__tipo_freno}"

class Cuadraciclo(Transporte):
    """
    Representa un cuadraciclo, motorizado de 4 ruedas
    Hereda de Transporte.
    """
    def __init__(self, placa, modelo, cilindrada):
        super().__init__(placa, modelo)
        self.__cilindrada = cilindrada

    @property
    def cilindrada(self): return self.__cilindrada

    def __str__(self):
        return super().__str__() + f" | Tipo: Cuadraciclo | Cilindrada: {self.__cilindrada}cc"

class Patineta(Transporte):
    """
    Representa una patineta, usualmente electrica.
    Hereda de Transporte.
    """
    def __init__(self, placa, modelo, es_electrica):
        super().__init__(placa, modelo)
        self.__es_electrica = es_electrica

    def __str__(self):
        electrica = "Sí" if self.__es_electrica else "No"
        return super().__str__() + f" | Tipo: Patineta | Eléctrica: {electrica}"