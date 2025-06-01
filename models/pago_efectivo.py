from metodos_pago import MetodoPago


class PagoEfectivo(MetodoPago):
    def __init__(self, metodo_id, nombre_visible, dni, nombre):
        super().__init__(metodo_id, nombre_visible)
        self.dni = dni
        self.nombre = nombre

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        if not dni or not dni.strip():
            raise ValueError("El campo dni no puede estar vacío")
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El campo nombre no puede estar vacío")
        self._nombre = nombre

    def pagar(self, monto: float):
        print(f"Pago en efectivo de {monto:.2f} realizado por {self.nombre} (DNI: {self.dni})")
        return True

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "dni": self.dni,
            "nombre": self.nombre
        })
        return data

    def __str__(self):
        return f"PagoEfectivo({self.metodo_id} - {self.nombre_visible} - {self.dni} - {self.nombre})"

    def __repr__(self):
        return f"PagoEfectivo('{self.metodo_id}', '{self.nombre_visible}', '{self.dni}', '{self.nombre}')"
