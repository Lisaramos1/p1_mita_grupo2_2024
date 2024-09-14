import datetime

def verificar_fecha_limite(fecha_prestamo, fecha_limite):
    return fecha_prestamo <= fecha_limite

# Fecha límite (por ejemplo, hasta el 31 de diciembre de 2024)
fecha_limite = datetime.date(2024, 12, 31)

# Fecha del préstamo actual
fecha_prestamo = datetime.date.today()

# Verificar si el préstamo está dentro del límite
if verificar_fecha_limite(fecha_prestamo, fecha_limite):
    print("Préstamo permitido.")
else:
    print("Préstamo no permitido, fecha fuera de límite.")