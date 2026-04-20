#Manejo del catalogo: carga, guardado y búsquedas

import json
import csv
import os
from modelos import VideoJuego, crear_juego


class Catalogo:
    """Administra la coleccion de videojuegos y persiste los cambios en archivo."""

    def __init__(self, archivo: str):
        self._archivo = archivo          # ruta real del archivo (json o csv)
        self._juegos: list[VideoJuego] = []
        self._cargar()

    # ------------------------------------------------------------------
    # Carga desde archivo
    # ------------------------------------------------------------------
    def _cargar(self):
        ext = os.path.splitext(self._archivo)[1].lower()
        try:
            if ext == ".json":
                self._cargar_json()
            elif ext == ".csv":
                self._cargar_csv()
            else:
                raise ValueError(f"Formato no soportado: {ext}")
            print(f"Catalogo cargado desde '{self._archivo}' ({len(self._juegos)} juegos).")
        except FileNotFoundError:
            print(f"Archivo '{self._archivo}' no encontrado. Se iniciara con catalogo vacio.")
        except Exception as e:
            print(f"Error al cargar catalogo: {e}")

    def _cargar_json(self):
        with open(self._archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for d in datos:
            self._juegos.append(crear_juego(d))

    def _cargar_csv(self):
        with open(self._archivo, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self._juegos.append(crear_juego(row))

    # ------------------------------------------------------------------
    # Guardado en archivo (SOBREESCRIBE el archivo original)
    # ------------------------------------------------------------------
    def guardar(self):
        ext = os.path.splitext(self._archivo)[1].lower()
        try:
            if ext == ".json":
                self._guardar_json()
            elif ext == ".csv":
                self._guardar_csv()
            print(f"Catalogo guardado en '{self._archivo}'.")
        except Exception as e:
            print(f"Error al guardar catálogo: {e}")

    def _guardar_json(self):
        datos = [j.to_dict() for j in self._juegos]
        with open(self._archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    def _guardar_csv(self):
        if not self._juegos:
            return
        campos = list(self._juegos[0].to_dict().keys())
        with open(self._archivo, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for j in self._juegos:
                writer.writerow(j.to_dict())

    # ------------------------------------------------------------------
    # Operaciones sobre el catalogo
    # ------------------------------------------------------------------
    def listar(self):
        if not self._juegos:
            print("El catalogo esta vacio.")
            return
        print(f"\n{'─'*90}")
        print(f"{'CATALOGO DE VIDEOJUEGOS':^90}")
        print(f"{'─'*90}")
        for j in self._juegos:
            print(j.mostrar_info())
        print(f"{'─'*90}")
        print(f"Total de juegos: {len(self._juegos)}\n")

    def buscar_por_nombre(self, termino: str) -> list[VideoJuego]:
        termino = termino.lower()
        return [j for j in self._juegos if termino in j.nombre.lower()]

    def buscar_por_categoria(self, categoria: str) -> list[VideoJuego]:
        return [j for j in self._juegos if j.categoria.lower() == categoria.lower()]

    def buscar_por_consola(self, consola: str) -> list[VideoJuego]:
        return [j for j in self._juegos if j.consola.lower() == consola.lower()]

    def buscar_por_id(self, id_buscado: int) -> VideoJuego | None:
        for j in self._juegos:
            if j.id == id_buscado:
                return j
        return None

    def id_existe(self, id_buscado: int) -> bool:
        return self.buscar_por_id(id_buscado) is not None

    def agregar(self, juego: VideoJuego):
        """Agrega un juego al catálogo Y sobreescribe el archivo."""
        if self.id_existe(juego.id):
            raise ValueError(f"Ya existe un juego con ID {juego.id}.")
        self._juegos.append(juego)
        self.guardar()   # ← persiste inmediatamente

    def siguiente_id(self) -> int:
        if not self._juegos:
            return 1
        return max(j.id for j in self._juegos) + 1

    def mostrar_resultados(self, lista: list[VideoJuego], etiqueta: str = "Resultados"):
        if not lista:
            print(f"No se encontraron resultados para '{etiqueta}'.")
            return
        print(f"\n{'─'*90}")
        print(f"  {etiqueta}")
        print(f"{'─'*90}")
        for j in lista:
            print(j.mostrar_info())
        print(f"{'─'*90}\n")
