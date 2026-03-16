# Importamos la clase base Animal desde el mismo paquete
from .animal import Animal

class Ave(Animal):
    """
    Representa la categoría de Aves.
    Hereda de Animal: nombre_individual y edad.
    """
    def __init__(self, nombre, edad, alas):
        # Inicializa los atributos de la clase padre Animal
        super().__init__(nombre, edad)
        # Atributo privado específico para aves
        self.__alas = alas

    @property
    def alas(self):
        "#Getter para la longitud de las alas en metros."""
        return self.__envergadura
    
    @alas.setter
    def alas(self, valor):
        #Setter para la longitud de las alas"""
        self.__alas = valor

    def __str__(self):
        """Sobrescribe __str__ concatenando la info de Animal con la de Ave."""
        return super().__str__() + f" | Clase: Ave | Longitud de las alas: {self.__envergadura}m"


class Pez(Animal):
    """
    Representa la categoría de Peces.
    Hereda de Animal.
    """
    def __init__(self, nombre, edad, tipo_agua):
        super().__init__(nombre, edad)
        # Atributo privado para el habitat acuatico
        self.__tipo_agua = tipo_agua

    @property
    def tipo_agua(self):
        #Getter para saber si es de agua Dulce o Salada."""
        return self.__tipo_agua
    
    @tipo_agua.setter
    def tipo_agua(self, valor):
        self.__tipo_agua = valor

    def __str__(self):
        return super().__str__() + f" | Clase: Pez | Agua: {self.__tipo_agua}"


class Reptil(Animal):
    """
    Representa la categoria de Reptiles.
    Hereda de Animal.
    """
    def __init__(self, nombre, edad, tipo_escamas):
        super().__init__(nombre, edad)
        # Atributo privado para la morfologia de la piel
        self.__tipo_escamas = tipo_escamas

    @property
    def tipo_escamas(self):
        #Getter para la descripcion de las escamas
        return self.__tipo_escamas
    
    @tipo_escamas.setter
    def tipo_escamas(self, v):
        self.__tipo_escamas = v

    def __str__(self):
        return super().__str__() + f" | Clase: Reptil | Escamas: {self.__tipo_escamas}"


class Anfibio(Animal):
    """
    Representa la categoria de Anfibios.
    Hereda de Animal.
    """
    def __init__(self, nombre, edad, tipo_piel):
        super().__init__(nombre, edad)
        # Atributo privado para la textura de la piel
        self.__tipo_piel = tipo_piel

    @property
    def tipo_piel(self):
        #Getter para la descripcion de la piel (ej. húmeda, lisa)
        return self.__tipo_piel

    @tipo_piel.setter
    def tipo_piel(self, v):
        self.__tipo_piel = v

    def __str__(self):
        return super().__str__() + f" | Clase: Anfibio | Piel: {self.__tipo_piel}"


class Mamifero(Animal):
    """
    Representa la categoria de Mamiferos.
    Hereda de Animal.
    """
    def __init__(self, nombre, edad, pelaje):
        super().__init__(nombre, edad)
        # Atributo privado para el tipo de pelaje
        self.__pelaje = pelaje

    @property
    def pelaje(self):
        #Getter para la descripcion del pelaje
        return self.__pelaje
    
    @pelaje.setter
    def pelaje(self, v):
        self.__pelaje = v

    def __str__(self):
        return super().__str__() + f" | Clase: Mamifero | Pelaje: {self.__pelaje}"