import re
import datetime

re_correo = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def validar_correo(correo: str) -> bool:
    result = re.match(re_correo, correo)
    return bool(result)


# Validar targeta crédito
def luhn_valido(numero: str) -> bool:
    total = 0
    reverse = numero[::-1]
    for i, d in enumerate(reverse):
        n = int(d)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


def tarjeta_vencida(vencimiento: str) -> bool:
    mes, anio = map(int, vencimiento.split("/"))
    anio += 2000
    hoy = datetime.date.today()
    fecha_venc = datetime.date(anio, mes, 1)
    return fecha_venc < hoy.replace(day=1)




