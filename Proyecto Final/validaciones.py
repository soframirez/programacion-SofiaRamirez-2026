# Funciones utilitarias de entrada y validacion

def leer_texto(prompt: str, requerido: bool = True) -> str:
    while True:
        valor = input(prompt).strip()
        if requerido and not valor:
            print("Este campo no puede estar vacío.")
            continue
        return valor


def leer_entero(prompt: str, minimo: int = 0) -> int:
    while True:
        try:
            valor = int(input(prompt).strip())
            if valor < minimo:
                print(f"Debe ser un numero >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("Ingrese un numero entero valido.")


def leer_flotante(prompt: str, minimo: float = 0.0) -> float:
    while True:
        try:
            valor = float(input(prompt).strip())
            if valor < minimo:
                print(f"Debe ser un numero >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("Ingrese un numero valido.")


def leer_opcion(prompt: str, opciones: list[str]) -> str:
    """Pide al usuario que elija una opción de una lista (case-insensitive)."""
    opciones_upper = [o.upper() for o in opciones]
    while True:
        valor = input(prompt).strip().upper()
        if valor in opciones_upper:
            return valor
        print(f"Opciones validas: {', '.join(opciones)}")


def leer_esrb(prompt: str = "ESRB Rating (E / E10+ / T / M / AO): ") -> str:
    return leer_opcion(prompt, ["E", "E10+", "T", "M", "AO"])


def leer_consola(prompt: str = "Consola (PS5 / XBOX / Nintendo): ") -> str:
    valor = leer_opcion(prompt, ["PS5", "XBOX", "NINTENDO"])
    return "Nintendo" if valor == "NINTENDO" else valor
