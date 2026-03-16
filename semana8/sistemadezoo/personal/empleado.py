class Empleado:
    """
    Clase padre que define la estructura base de un trabajador del zoo
    """
    def __init__(self, nombre, id_empleado):
        # Atributos privados
        self.__nombre = nombre
        self.__id_empleado = id_empleado

    @property
    def nombre(self):
       #Getter para acceder al nombre privado
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        #Setter para modificar el nombre
        if valor.strip():
            self.__nombre = valor

    @property
    def id_empleado(self):
        #Getter para acceder al ID 
        return self.__id_empleado

    @id_empleado.setter
    def id_empleado(self, valor):
        #Setter para modificar el ID
        self.__id_empleado = valor

    def __str__(self):
        #Metodo para representar al empleado como texto
        return f"ID: {self.__id_empleado} | Nombre: {self.__nombre}"