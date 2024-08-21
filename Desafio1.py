import random
Estudiantes = ['Estudiante 1','Estudiante 2','Estudiante 3']
Materias = ['Materia 1','Materia 2','Materia 3']
matriz = [[0] * len(Estudiantes) for _ in range(len(Materias))] # inicializo la lista de listas que tambien es considerada una matriz
Cantestu = len(Estudiantes)
CantMate = len(Materias)
def mostrarmatriz(): #funcion que muestra la matriz ordenada
    print(f"{'Id':<15}", end="")
    for materia in Materias:
        print(f"{materia:<15}", end="")
    print()
    for j in range(Cantestu):
        print(f"{Estudiantes[j]:<15}", end="")
        for i in range(CantMate):
            print(f"{matriz[i][j]:<15}", end="")
        print()

def calcularpromedioestudiantes(): #funcion que calcula el promedio de las notas de cada estudiante
    for i in range(Cantestu):
        nota=0
        for j in range(CantMate):
            nota += matriz[j][i]
        promedio = (nota//CantMate)*10
        print(f"el promedio del {Estudiantes[i]:<15} es:", end='')
        print(promedio,'%')

def calcularpromediomaterias(): #funcion que calcula el promedio de las notas de cada materia
    for i in range(CantMate):
        nota=0
        for j in range(Cantestu):
            nota += matriz[j][i]
        promedio = (nota//Cantestu)*10
        print(f"el promedio de la {Materias[i]:<15} es:", end='')
        print(promedio,'%')

# codigo main
for i in range(CantMate):
    for j in range(Cantestu):
        matriz[i][j]= random.randint(1,10)
mostrarmatriz()
calcularpromedioestudiantes()
calcularpromediomaterias()