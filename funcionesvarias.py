Personas=[
     [5005, 'Juan Perez', 12345678],
    [5006, 'Ana Gomez', 23456789],
    [5007, 'Luis Martinez', 34567890],
    [5008, 'Maria Lopez', 45678901],
    [5009, 'Carlos Sanchez', 56789012]
]

#A BORRAR
discos =[
    {'Id':1,'nombre':'Disco 1','Artista':"A",'Genero':'Rock','Cantidad':1},
    {'Id':2,'nombre':'Disco 2','Artista':"B",'Genero':'Pop','Cantidad':3},
    {'Id':3,'nombre':'Disco 3','Artista':"C",'Genero':'Techno','Cantidad':2},
    {'Id':4,'nombre':'Disco 4','Artista':"D",'Genero':'Dubstep','Cantidad':7},
    {'Id':5,'nombre':'Disco 5','Artista':"E",'Genero':'Rock nacional','Cantidad':1},
    {'Id':6,'nombre':'Disco 6','Artista':"F",'Genero':'Rock cristiano alternativo','Cantidad':4},
    {'Id':7,'nombre':'Disco 7','Artista':"G",'Genero':'Trap','Cantidad':6},
    {'Id':8,'nombre':'Disco 8','Artista':"H",'Genero':'Cumbia','Cantidad':2},
    {'Id':9,'nombre':'Disco 9','Artista':"I",'Genero':'Indie','Cantidad':8},
    {'Id':10,'nombre':'Disco 10','Artista':"J",'Genero':'rock','Cantidad':3}
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

def disponibilidadalbum(indicemenu,busqueda,listadiccionario):
    if indicemenu==1: #Busqueda por id 
        busqueda=int(busqueda)
        lista=list(filter(lambda x: x.get("Id")==busqueda and x.get("cantidad".lower())!=0,discos))
    elif indicemenu==2: #Busqueda por nombre del disco 
        busqueda=busqueda.lower()
        lista=list(filter(lambda x: x.get("Nombre","").lower()==busqueda and x.get("Cantidad".lower())!=0,discos))
    elif indicemenu==3: #Busqueda por artista
        busqueda=busqueda.lower() 
        lista=list(filter(lambda x: x.get("Artista","").lower()==busqueda and x.get("Cantidad".lower())!=0,discos))
    elif indicemenu==4: #Busqueda por genero
        busqueda=busqueda.lower() 
        lista=list(filter(lambda x: x.get("Genero","").lower()==busqueda and x.get("Cantidad".lower())!=0,discos))
    
    if lista :    
        for i in lista :
            print(i)
    else:
        print('No se encontraron discos disponibles.')
        return 0
    
    
    id=int(input("Ingrese el id del disco que desea retirar"))
    while not any(listadiccionario["id"]==id for dicionarios in listadiccionario ):
        print("ID de usuario no encontrado, intentelo de nuevo.")
        id=int(input("Ingrese el id del disco que desea retirar"))
   
    diccionarioamodificar=discos[id-1]
    diccionarioamodificar["Cantidad" .lower()]-=1

    print(discos)
          
    
disponibilidadalbum(4,"rock",discos)