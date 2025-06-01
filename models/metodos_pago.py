import datetime
from abc import ABC, abstractmethod


class MetodoPago(ABC):
    def __init__(self, metodo_id, nombre_visible):
        self.metodo_id = metodo_id
        self.nombre_visible = nombre_visible
        self.fecha = datetime.datetime.now()

    @abstractmethod
    def pagar(self, monto):
        pass

    @property
    def metodo_id(self):
        return self._metodo_id

    @metodo_id.setter
    def metodo_id(self, metodo_id):
        if not metodo_id.split():
            raise ValueError("El metodo_id no puede estar vacio")
        else:
            self._metodo_id = metodo_id

    @property
    def nombre_visible(self):
        return self._nombre_visible

    @nombre_visible.setter
    def nombre_visible(self, nombre_visible):
        if not nombre_visible.split():
            raise ValueError("El campo visible no puede estar vacio")
        else:
            self._nombre_visible = nombre_visible

    def to_dict(self):
        return {
            "metodo_id": {self.metodo_id},
            "nombre_visible": {self.nombre_visible},
            "fecha": {self.fecha}
        }

    def __str__(self):
        return f"MetodoPago({self.metodo_id} - {self.nombre_visible} - {self.fecha})"

    def __repr__(self):
        return f"MetofoPago('{self.metodo_id}', '{self.nombre_visible}', '{self.fecha}')"
