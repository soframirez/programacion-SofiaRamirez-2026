class Contacto:
    def __init__(self, nombre, telefono, email, edad, residencia):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.edad = int(edad)
        self.residencia = residencia

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"{self.nombre.ljust(15)} | {self.telefono.ljust(10)} | {self.email.ljust(20)} | {self.edad} anhos | {self.residencia}"