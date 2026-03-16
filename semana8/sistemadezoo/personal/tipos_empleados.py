# Importa la clase padre Empleado
from .empleado import Empleado

class Administrador(Empleado):
    """
    Representa al personal administrativo
    Hereda de Empleado: nombre e id_empleado.
    """
    def __init__(self, nombre, id_empleado, departamento):
        super().__init__(nombre, id_empleado)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, valor):
        self.__departamento = valor

    def __str__(self):
        return super().__str__() + f" | Puesto: Administrador | Depto: {self.__departamento}"


class Guardian(Empleado):
    """
    Representa al personal de seguridad y vigilancia
    Hereda de Empleado.
    """
    def __init__(self, nombre, id_empleado, turno):
        super().__init__(nombre, id_empleado)
        self.__turno = turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, valor):
        self.__turno = valor

    def __str__(self):
        return super().__str__() + f" | Puesto: Guardian | Turno: {self.__turno}"


class Veterinario(Empleado):
    """
    Representa al personal veterinario
    Hereda de Empleado.
    """
    def __init__(self, nombre, id_empleado, especialidad):
        super().__init__(nombre, id_empleado)
        self.__especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        self.__especialidad = valor

    def __str__(self):
        return super().__str__() + f" | Puesto: Veterinario | Especialidad: {self.__especialidad}"


class Conserje(Empleado):
    """
    Representa al personal encargado del mantenimiento de instalaciones.
    Hereda de Empleado.
    """
    def __init__(self, nombre, id_empleado, area_asignada):
        super().__init__(nombre, id_empleado)
        self.__area_asignada = area_asignada

    @property
    def area_asignada(self):
        return self.__area_asignada

    @area_asignada.setter
    def area_asignada(self, valor):
        self.__area_asignada = valor

    def __str__(self):
        return super().__str__() + f" | Puesto: Conserje | Área: {self.__area_asignada}"