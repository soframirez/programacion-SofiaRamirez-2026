#Clase para ejemplo de composicion
class Motor:
    def __init__(self, tipo, caballos):
        self.__tipo = tipo
        self.__caballos = caballos

    def get_info(self):
        return f"Motor {self.__tipo} de {self.__caballos} CV"