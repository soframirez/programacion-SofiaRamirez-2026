# Definicion de la clase para representar una mascota
class Mascota:
    # Metodo para crear los datos de la mascota
    def __init__(self, nombre, especie, raza):
        # Se guardan los datos en los atributos privados de la clase
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza

    # Getters
    def get_nombre(self): return self.__nombre
    def get_especie(self): return self.__especie
    def get_raza(self): return self.__raza

    # Setters
    def set_nombre(self, n): self.__nombre = n
    def set_especie(self, e): self.__especie = e
    def set_raza(self, r): self.__raza = r

    def __str__(self):
        return f"Mascota: {self.__nombre} ({self.__especie})"

    def __len__(self):
        # Retorna el largo del nombre
        return len(self.__nombre)