Personas=[
     [5005, 'Juan Perez', 12345678],
    [5006, 'Ana Gomez', 23456789],
    [5007, 'Luis Martinez', 34567890],
    [5008, 'Maria Lopez', 45678901],
    [5009, 'Carlos Sanchez', 56789012]
]

def generadorid (matriz):
    """
    pre: recibe una matriz
    pos: Devuelve el numero de id mediante el len de la lista
    """
    len_lista=len(matriz)+1
    id=f"{len_lista:04}"
    return id 

def existenciaenmatrix(userid,matriz):
    """
    pre:Recibe el userid y la matriz
    pos:Si se encuetra el userdi== True ,, si no lo encuentra==False
    """
    cont=0
    
    while cont<len(matriz): 
        if matriz[cont][0] == userid:
            return True
        else:   
            cont+=1
    return False

def disponibilidadalbum(indicemenu,busqueda,diccionario):
    if indicemenu==1:
        busqueda=int(busqueda)
    
    
    return idalbum