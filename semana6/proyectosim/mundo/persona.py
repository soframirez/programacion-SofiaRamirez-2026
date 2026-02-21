# Definicion de la clase para representar una persona
class Personita:
    # Metodo para crear el objeto
    def __init__(self, nombre, edad, profesion):
        # Se guardan los datos en los atributos del objeto
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    # Metodo especial para definir como se vera el objeto al imprimirlo
    def __str__(self):
        # Retorna una cadena de texto con la informacion formateada
        return f"Persona: {self.nombre} | Edad: {self.edad} | Profesion: {self.profesion}"
    