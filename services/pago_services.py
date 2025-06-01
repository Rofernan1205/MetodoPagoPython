from utils.validadores import tarjeta_vencida, luhn_valido

class PagoService:
    def procesar_pago(self, tarjeta, monto: float):
        if tarjeta_vencida(tarjeta.vencimiento):
            raise ValueError("La tarjeta está vencida.")
        if not luhn_valido(tarjeta.numero):
            raise ValueError("Número de tarjeta inválido (falló Luhn).")

        # Aquí iría lógica para consultar si tiene saldo (simulado)
        if monto > 1000:
            raise ValueError("Fondos insuficientes.")

        return tarjeta.pagar(monto)
