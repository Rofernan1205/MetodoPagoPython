from metodos_pago import MetodoPago
from utils import validadores

class Paypal(MetodoPago):
    def __init__(self,metodo_id, nombre_visible,  correo):
        super().__init__(metodo_id, nombre_visible)
        self.correo = correo

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, correo):
        if not  validadores.validar_correo(correo):
            raise ValueError("Correo inválido.")
        else:
            self._correo = correo

    def pagar(self, monto: float) -> bool:
        print(f"Pago por PayPal de {monto:.2f} realizado por {self.correo}")
        return True

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({
            "correo": self.correo
        })
        return data

    def __str__(self) -> str:
        return f"Paypal({self.metodo_id} - {self.nombre_visible} - {self.correo})"


    def __repr__(self) -> str:
        return f"Paypal('{self.metodo_id}', '{self.nombre_visible}', '{self.correo}')"

