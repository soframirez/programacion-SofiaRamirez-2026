import math
from abc import ABC, abstractmethod

# Clase Base 

class Figura(ABC):
    """
    Clase abstracta que sirve como molde para cualquier figura geometrica 3D.
    """
    @abstractmethod
    def volumen(self):
        """
        Metodo obligatorio que todas las subclases deben implementar
        para calcular su volumen específico.
        """
        pass

# Implementacion de Figuras 

class Cubo(Figura):
    """Representa un cubo donde todos sus lados son iguales."""
    def __init__(self, lado):
        self.lado = lado

    def volumen(self):
        # El volumen de un cubo es lado elevado al cubo (L**3)
        return self.lado ** 3

class Paralelepipedo(Figura):
    """Representa un paralelepipedo."""
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def volumen(self):
        # Multiplicacion de las tres dimensiones espaciales
        return self.largo * self.ancho * self.alto

class Cilindro(Figura):
    """Representa un cilindro circular recto."""
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        # Area del circulo (π * r**2) multiplicada por la altura (h)
        return math.pi * (self.radio ** 2) * self.altura

class Esfera(Figura):
    """Representa una esfera perfecta."""
    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        # Formula estandar: 4/3 * π * r**3
        return (4/3) * math.pi * (self.radio ** 3)

class Cono(Figura):
    """Representa un cono circular recto."""
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        # El volumen de un cono es un tercio del de un cilindro con igual base y altura
        return (1/3) * math.pi * (self.radio ** 2) * self.altura