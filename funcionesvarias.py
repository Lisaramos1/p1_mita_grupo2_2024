
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
        lista=list(filter(lambda x: x.get("Id")==busqueda and x.get("cantidad".lower())!=0,listadiccionario))
    elif indicemenu==2: #Busqueda por nombre del disco 
        busqueda=busqueda.lower()
        lista=list(filter(lambda x: x.get("Nombre","").lower()==busqueda and x.get("Cantidad".lower())!=0,listadiccionario))
    elif indicemenu==3: #Busqueda por artista
        busqueda=busqueda.lower() 
        lista=list(filter(lambda x: x.get("Artista","").lower()==busqueda and x.get("Cantidad".lower())!=0,listadiccionario))
    elif indicemenu==4: #Busqueda por genero
        busqueda=busqueda.lower() 
        lista=list(filter(lambda x: x.get("Genero","").lower()==busqueda and x.get("Cantidad".lower())!=0,listadiccionario))
    
    if len(lista)>0 :    
        for i in lista :
            print(i)
    else:
        print('No se encontraron discos disponibles.')
        return 0
    
    id_encontrado=False
    
    while not id_encontrado:
        id=int(input("Ingrese el id del disco que desea retirar"))
        control=False
        
        for i in listadiccionario: #Busamos el id ingresado por el usuario dentro del stock 
            if i["id"]==id:
                diccionarioamodificar=listadiccionario[id-1]
                diccionarioamodificar["cantidad"]-=1
                print("stock actualizado")
                control=True
        
        if control:
            id_encontrado=True
        else:        
            print("ID de usuario no encontrado, intentelo de nuevo.")
            id=int(input("Ingrese el id del disco que desea retirar"))
   
    
    print(f"Este es el nuevo stock del discio {diccionarioamodificar}")
    print()
