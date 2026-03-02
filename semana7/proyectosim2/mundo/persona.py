# Definicion de la clase para representar una persona
class Personita:
    # Metodo para crear el objeto
    def __init__(self, nombre, edad, profesion):
        # Atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__profesion = profesion
        # Asociacion: Una persona puede tener una mascota (empieza en None)
        self.__mascota_asociada = None

    # Getters
    def get_nombre(self): return self.__nombre
    def get_edad(self): return self.__edad
    def get_profesion(self): return self.__profesion
    def get_mascota(self): return self.__mascota_asociada

    # Setters
    def set_nombre(self, nombre): self.__nombre = nombre
    def set_edad(self, edad): self.__edad = edad
    def set_profesion(self, prof): self.__profesion = prof
    def set_mascota(self, mascota): self.__mascota_asociada = mascota

    def __str__(self):
        msg = f"Persona: {self.__nombre} | Profesion: {self.__profesion}"
        if self.__mascota_asociada:
            msg += f" | Tiene a: {self.__mascota_asociada.get_nombre()}"
        return msg

    def __len__(self):
        # Retorna la edad como medida de vida
        return int(self.__edad)
    