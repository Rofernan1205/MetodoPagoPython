from abc import ABC, abstractmethod


class MetodoPago(ABC):
    def __init__(self, metodo_id, nombre_visible):
        self.metodo_id = metodo_id
        self.nombre_visible = nombre_visible

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
        if not nombre_visible.split() or not nombre_visible:
            raise ValueError("El campo visible no puede estar vacio")
        else:
            self._nombre_visible = nombre_visible

    @abstractmethod
    def pagar(self, monto: float):
        pass

    @property
    def tipo(self):
        return self.__class__.__name__.lower() # la clase padre y las hijas van a debolver campo tipo en minusculas

    def to_dict(self):
        return {
            "metodo_id": self.metodo_id,
            "tipo": self.tipo,
            "nombre_visible": self.nombre_visible,
        }

    def __str__(self) -> str:
        return f"MetodoPago({self.metodo_id} - {self.nombre_visible})"

    def __repr__(self) -> str:
        return f"MetodoPago('{self.metodo_id}', '{self.nombre_visible}')"

