import datetime

def verificar_fecha_limite(fecha_prestamo, fecha_limite):
    return fecha_prestamo <= fecha_limite

# Fecha límite corregida (por ejemplo, 14 de septiembre de 2024)
fecha_limite = datetime.date(2024, 9, 14)

# Sumar 30 días a la fecha límite
fecha_limite_con_30_dias = fecha_limite + datetime.timedelta(days=30)

# Fecha del préstamo actual
fecha_prestamo = datetime.date.today()

# Verificar si el préstamo está dentro del nuevo límite
if verificar_fecha_limite(fecha_prestamo, fecha_limite_con_30_dias):
    print("Préstamo permitido.")
else:
    print("Préstamo no permitido, fecha fuera de límite.")
