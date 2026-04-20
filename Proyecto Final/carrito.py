# Logica del carrito de compras
from modelos import VideoJuego


class ItemCarrito:
    """Representa un videojuego dentro del carrito con su cantidad."""

    def __init__(self, juego: VideoJuego, cantidad: int = 1):
        self._juego = juego
        self._cantidad = cantidad

    @property
    def juego(self):
        return self._juego

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor < 1:
            raise ValueError("La cantidad debe ser al menos 1.")
        self._cantidad = valor

    @property
    def subtotal(self):
        return self._juego.precio * self._cantidad

    def __str__(self):
        return (
            f"  {self._juego.nombre[:40]:<40} x{self._cantidad}  "
            f"${self._juego.precio:.2f} c/u  →  ${self.subtotal:.2f}"
        )


class Carrito:
    """Administra los items seleccionados para la compra."""

    def __init__(self):
        self._items: dict[int, ItemCarrito] = {}   # id → ItemCarrito


    def agregar(self, juego: VideoJuego, cantidad: int = 1):
        if cantidad < 1:
            raise ValueError("La cantidad debe ser al menos 1.")
        if juego.stock < cantidad:
            raise ValueError(
                f"Stock insuficiente. Disponible: {juego.stock}, solicitado: {cantidad}."
            )
        if juego.id in self._items:
            nueva_cant = self._items[juego.id].cantidad + cantidad
            if juego.stock < nueva_cant:
                raise ValueError(
                    f"Stock insuficiente. Disponible: {juego.stock}, "
                    f"ya en carrito: {self._items[juego.id].cantidad}."
                )
            self._items[juego.id].cantidad = nueva_cant
            print(f"Cantidad actualizada: {juego.nombre} x{nueva_cant}")
        else:
            self._items[juego.id] = ItemCarrito(juego, cantidad)
            print(f"Agregado al carrito: {juego.nombre}")

    def eliminar(self, id_juego: int):
        if id_juego not in self._items:
            raise ValueError(f"El juego con ID {id_juego} no esta en el carrito.")
        nombre = self._items[id_juego].juego.nombre
        del self._items[id_juego]
        print(f"Eliminado del carrito: {nombre}")

    def mostrar(self):
        if not self._items:
            print("\nEl carrito esta vacio.\n")
            return
        print(f"\n{'─'*70}")
        print(f"{'CARRITO DE COMPRAS':^70}")
        print(f"{'─'*70}")
        for item in self._items.values():
            print(item)
        print(f"{'─'*70}")
        print(f"  {'TOTAL A PAGAR':>50}   ${self.total:.2f}")
        print(f"{'─'*70}\n")

    def vaciar(self):
        self._items.clear()

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self._items.values())

    @property
    def items(self) -> list[ItemCarrito]:
        return list(self._items.values())

    @property
    def esta_vacio(self) -> bool:
        return len(self._items) == 0
