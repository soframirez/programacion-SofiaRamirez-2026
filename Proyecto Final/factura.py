#Generacion de facturas en CSV o JSON

import json
import csv
from datetime import datetime
from carrito import Carrito


class Factura:
    """Genera una factura a partir del carrito."""

    def __init__(self, cliente: str, carrito: Carrito):
        if not cliente or not cliente.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")
        if carrito.esta_vacio:
            raise ValueError("El carrito está vacío. No se puede generar factura.")
        self._cliente = cliente.strip()
        self._fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._items = carrito.items
        self._total = carrito.total


    def _datos_items(self) -> list[dict]:
        return [
            {
                "nombre": item.juego.nombre,
                "consola": item.juego.consola,
                "precio_unitario": item.juego.precio,
                "cantidad": item.cantidad,
                "subtotal": item.subtotal
            }
            for item in self._items
        ]

    def guardar_json(self, nombre_archivo: str):
        if not nombre_archivo.endswith(".json"):
            nombre_archivo += ".json"
        datos = {
            "cliente": self._cliente,
            "fecha": self._fecha,
            "juegos": self._datos_items(),
            "total": round(self._total, 2)
        }
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
        print(f"Factura guardada en '{nombre_archivo}'")

    def guardar_csv(self, nombre_archivo: str):
        if not nombre_archivo.endswith(".csv"):
            nombre_archivo += ".csv"
        with open(nombre_archivo, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            # Encabezado con datos del cliente
            writer.writerow(["Cliente", self._cliente])
            writer.writerow(["Fecha", self._fecha])
            writer.writerow([])
            # Detalle de productos
            writer.writerow(["Nombre", "Consola", "Precio Unitario", "Cantidad", "Subtotal"])
            for item in self._datos_items():
                writer.writerow([
                    item["nombre"],
                    item["consola"],
                    f"${item['precio_unitario']:.2f}",
                    item["cantidad"],
                    f"${item['subtotal']:.2f}"
                ])
            writer.writerow([])
            writer.writerow(["", "", "", "TOTAL", f"${self._total:.2f}"])
        print(f"Factura guardada en '{nombre_archivo}'")

    def mostrar_pantalla(self):
        print(f"\n{'═'*60}")
        print(f"{'FACTURA':^60}")
        print(f"{'═'*60}")
        print(f"  Cliente : {self._cliente}")
        print(f"  Fecha   : {self._fecha}")
        print(f"{'─'*60}")
        print(f"  {'Producto':<35} {'Cant':>4}  {'Precio':>8}  {'Subtotal':>9}")
        print(f"{'─'*60}")
        for item in self._items:
            print(
                f"  {item.juego.nombre[:35]:<35} {item.cantidad:>4}  "
                f"${item.juego.precio:>7.2f}  ${item.subtotal:>8.2f}"
            )
        print(f"{'─'*60}")
        print(f"  {'TOTAL A PAGAR':>50}  ${self._total:.2f}")
        print(f"{'═'*60}\n")
