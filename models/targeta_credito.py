import re
from operator import truediv

from metodos_pago import  MetodoPago

class TargetaCredito(MetodoPago):
    def __init__(self, metodo_id, nombre_visible, numero, vencimiento, cvv, saldo):
        super().__init__(metodo_id, nombre_visible)
        self.numero = numero
        self.vencimiento = vencimiento
        self.cvv = cvv
        self.saldo = saldo


    @property
    def numero(self) -> str:
        return  self._numero

    @numero.setter
    def numero(self, numero):
        if not numero.isdigit() or len(numero) != 16:
            raise ValueError("Número de tarjeta inválida.")
        else:
            self._numero = numero

    @property
    def vencimiento(self):
        return self._vencimiento

    @vencimiento.setter
    def vencimiento(self, fecha):
        if not re.fullmatch(r"\d{2}/\d{2}", fecha):
            raise ValueError("El venciento debe estar en el formato MM/AA")
        else:
            self._vencimiento = fecha

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        if not re.fullmatch(r"\d{3,4}", cvv):
            raise ValueError("El CVV debe tener 3 o 4 dígitos.")
        self._cvv = cvv

    def pagar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Pago {monto} realizado. Saldo restante : {self.saldo}")
            return True
        else:
            print("Fondo insuficiente")
            return False



    def to_dict(self):
        data = super().to_dict()
        data.update(
            {
                "numero" : "**** **** **** " + self.numero[-4:],
                "vencimiento" : self.vencimiento
            }
        )
        return data

    def __str__(self):
        return (f"TargetaCredito({self.metodo_id} - {self.nombre_visible} - {self.numero}"
                f"- {self.vencimiento} - {self.cvv})")

    def __repr__(self):
        return (f"TargetaCredito('{self.metodo_id}', '{self.nombre_visible}', '{self.numero}', )"
                f"'{self.vencimiento}', '{self.cvv}'")


