import random

estudiantes, asignaturas = [1001, 1002, 1003, 1004], ["pr1", "pr2", "pr3"]

def crear_matriz():
    filas = len(estudiantes) + 1
    columnas = len(asignaturas) + 1
    return [[0] * columnas for _ in range(filas)]

def agregar_encabezados(m):
    for f in range(1, len(asignaturas) + 1):
        m[0][f] = asignaturas[f - 1]

    for f in range(1, len(estudiantes) + 1):
        m[f][0] = estudiantes[f - 1]

def llenar_matriz(m):
    agregar_encabezados(m)
    for f in range(1, len(estudiantes) + 1):
        for c in range(1, len(asignaturas) + 1):
            m[f][c] = random.randint(1, 9)

def mostrar_matriz(m):
    for fila in m:
        for valor in fila:
            print(f"{valor:3}", end=" ")
        print()

def prom_materias(m):
    for c in range(1, len(m[0])):
        suma = 0
        for f in range(1, len(m)):
            suma += m[f][c]
        promedio = suma // (len(m) - 1)
        print(f"Promedio de materia {c}: {promedio}")

def prom_estudiantes(m):
    for f in range(1, len(m)):
        suma = 0
        for c in range(1, len(m[0])):
            suma += m[f][c]
        promedio = suma // (len(m[0]) - 1)
        print(f"Promedio del estudiante {f}: {promedio}")

matriz = crear_matriz()
llenar_matriz(matriz)
mostrar_matriz(matriz)
prom_materias(matriz)
prom_estudiantes(matriz)
