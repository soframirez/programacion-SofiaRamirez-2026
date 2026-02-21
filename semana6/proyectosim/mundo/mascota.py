# Definicion de la clase para representar una mascota
class Mascota:
    # Metodo para crear los datos de la mascota
    def __init__(self, nombre, especie, raza):
        # Se guardan los datos en los atributos de la clase
        self.nombre = nombre
        self.especie = especie
        self.raza = raza

    # Metodo para mostrar la informacion de la mascota como texto
    def __str__(self):
        # Retorna el nombre, especie y raza formateados
        return f"Mascota: {self.nombre} ({self.especie}, {self.raza})"