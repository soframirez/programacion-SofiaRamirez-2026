import math

def calcular_cubo(lado):
    return lado**3

def calcular_paralelepipedo(largo, ancho, altura):
    return largo * ancho * altura

def calcular_cilindro(radio, altura):
    return math.pi * (radio**2) * altura

def calcular_esfera(radio):
    return (4/3) * math.pi * (radio**3)

def calcular_cono(radio, altura):
    return (1/3) * math.pi * (radio**2) * altura