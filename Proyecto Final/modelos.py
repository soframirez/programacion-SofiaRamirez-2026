# Clases de videojuegos con herencia, encapsulamiento y @property

class VideoJuego:
    """Clase padre que representa un videojuego."""

    def __init__(self, id, nombre, categoria, precio, esrb, stock, consola):
        self._id = id
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._esrb = esrb
        self._stock = stock
        self._consola = consola

    # --- Properties ---
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        if not valor or not valor.strip():
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    @property
    def esrb(self):
        return self._esrb

    @esrb.setter
    def esrb(self, valor):
        ratings_validos = ["E", "E10+", "T", "M", "AO"]
        if valor not in ratings_validos:
            raise ValueError(f"ESRB inválido. Opciones: {ratings_validos}")
        self._esrb = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    @property
    def consola(self):
        return self._consola

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "categoria": self._categoria,
            "precio": self._precio,
            "esrb": self._esrb,
            "stock": self._stock,
            "consola": self._consola
        }

    def mostrar_info(self):
        """Polimorfismo: cada subclase puede personalizar esto."""
        return (
            f"[{self._consola}] ID:{self._id} | {self._nombre} "
            f"| {self._categoria} | ${self._precio:.2f} "
            f"| ESRB:{self._esrb} | Stock:{self._stock}"
        )

    def __str__(self):
        return self.mostrar_info()


class JuegoPS5(VideoJuego):
    """Videojuego para PlayStation 5"""

    def __init__(self, id, nombre, categoria, precio, esrb, stock):
        super().__init__(id, nombre, categoria, precio, esrb, stock, "PS5")

    def mostrar_info(self):
        return f"PS5  | {super().mostrar_info()}"


class JuegoXbox(VideoJuego):
    """Videojuego para Xbox"""

    def __init__(self, id, nombre, categoria, precio, esrb, stock):
        super().__init__(id, nombre, categoria, precio, esrb, stock, "XBOX")

    def mostrar_info(self):
        return f"XBOX | {super().mostrar_info()}"


class JuegoNintendo(VideoJuego):
    """Videojuego para Nintendo Switch"""

    def __init__(self, id, nombre, categoria, precio, esrb, stock):
        super().__init__(id, nombre, categoria, precio, esrb, stock, "Nintendo")

    def mostrar_info(self):
        return f"NIN  | {super().mostrar_info()}"


def crear_juego(data: dict) -> VideoJuego:
    """Factory: instancia la subclase correcta segun la consola."""
    consola = data["consola"].strip().upper()
    
    args = (
        int(data["id"]),   
        data["nombre"],
        data["categoria"],
        float(data["precio"]), 
        data["esrb"],
        int(data["stock"]),  
    )
    
    if consola == "PS5":
        return JuegoPS5(*args)
    elif consola == "XBOX":
        return JuegoXbox(*args)
    elif consola == "NINTENDO":
        return JuegoNintendo(*args)
    else:
        return VideoJuego(*(args + (consola,)))