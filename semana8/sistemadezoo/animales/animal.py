class Animal:
    """
    Clase padre para todos los animales del zoológico.
    Define atributos comunes como especie y edad.
    """
    def __init__(self, nombre_individual, edad):
        self.__nombre_individual = nombre_individual
        self.__edad = edad

    @property
    def nombre_individual(self):
        return self.__nombre_individual

    @nombre_individual.setter
    def nombre_individual(self, valor):
        self.__nombre_individual = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        # El setter actua como filtro de calidad (no permite edades negativas)
        if valor >= 0:
            self.__edad = valor

    def __str__(self):
        #Metodo dunder para imprimir la informacion
        return f"Nombre: {self.__nombre_individual} | Edad: {self.__edad}"

