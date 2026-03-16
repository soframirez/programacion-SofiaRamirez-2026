# Importación de las clases de categoría desde el módulo local
from .categorias import Reptil, Mamifero, Ave, Pez, Anfibio

class Serpiente(Reptil):
    """
    Representa la especie especifica Serpiente.
    Hereda de Reptil -> Animal
    """
    def __init__(self, nombre, edad, escamas, longitud):
        # super() traslada los datos a la clase Reptil y esta a Animal
        super().__init__(nombre, edad, escamas)
        # Atributo privado especifico de esta especie
        self.__longitud = longitud

    @property
    def longitud(self):
        """Getter para la longitud de la serpiente"""
        return self.__longitud
    
    @longitud.setter
    def longitud(self, v):
        """Setter para modificar la logintud"""
        self.__longitud = v

    def __str__(self):
        """Retorna los datos heredados"""
        return super().__str__() + f" | Especie: Serpiente | Largo: {self.__longitud}m"


class Leon(Mamifero):
    """
    Representa la especie especifica Leon.
    Hereda de Mamifero -> Animal.
    """
    def __init__(self, nombre, edad, pelaje, rugido_db):
        super().__init__(nombre, edad, pelaje)
        self.__rugido_db = rugido_db

    @property
    def rugido_db(self):
        """Getter para laa potencia del rugido"""
        return self.__rugido_db
    
    @rugido_db.setter
    def rugido_db(self, v):
        self.__rugido_db = v

    def __str__(self):
        return super().__str__() + f" | Especie: Leon | Rugido: {self.__rugido_db}"


class Aguila(Ave):
    """
    Representa la especie especifica Aguila.
    Hereda de Ave -> Animal.
    """
    def __init__(self, nombre, edad, envergadura, tipo_vuelo):
        super().__init__(nombre, edad, envergadura)
        self.__tipo_vuelo = tipo_vuelo

    @property
    def tipo_vuelo(self):
        """Getter para el estilo de vuelo"""
        return self.__tipo_vuelo
    
    @tipo_vuelo.setter
    def tipo_vuelo(self, v):
        self.__tipo_vuelo = v

    def __str__(self):
        return super().__str__() + f" | Especie: Aguila | Vuelo: {self.__tipo_vuelo}"


class Tiburon(Pez):
    """
    Representa la especie especifica Tiburon.
    Hereda de Pez -> Animal.
    """
    def __init__(self, nombre, edad, agua, num_dientes):
        super().__init__(nombre, edad, agua)
        self.__num_dientes = num_dientes

    @property
    def num_dientes(self):
        """Getter para la cantidad de dientes"""
        return self.__num_dientes
    
    @num_dientes.setter
    def num_dientes(self, v):
        self.__num_dientes = v

    def __str__(self):
        return super().__str__() + f" | Especie: Tiburon | Dientes: {self.__num_dientes}"


class Rana(Anfibio):
    """
    Representa la especie especifica Rana.
    Hereda de Anfibio -> Animal.
    """
    def __init__(self, nombre, edad, piel, color):
        super().__init__(nombre, edad, piel)
        self.__color = color

    @property
    def color(self):
        """Getter para el color de la piel"""
        return self.__color
    
    @color.setter
    def color(self, v):
        self.__color = v

    def __str__(self):
        return super().__str__() + f" | Especie: Rana | Color: {self.__color}"