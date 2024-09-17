
def generadorid (matriz):
    """
    pre: recibe una matriz
    pos: Devuelve el numero de id mediante el len de la lista
    """
    len_lista=len(matriz)+1
    id=f"{len_lista:04}"
    return id

def imprimir_matriz(matriz):
    print()
    for fila in matriz:
        print("||".join(map(str,fila)))



#busquedas de albums
def menu_busqueda_album():
    print('1 Id del disco ')
    print('2 Nombre del disco ')
    print('3 Nombre del artista ')
    print('4 Genero del album ')
    print()

def filtros_busqueda(indicemenu,busqueda,listadiccionario): #uso de funciones lambda y metodos de strings
    if indicemenu==1: #Busqueda por id 
        busqueda=int(busqueda)
        lista=list(filter(lambda x: x.get("id")==busqueda and x.get("cantidad".lower())!=0,listadiccionario))
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
        for disco in lista:
            print(f"ID: {disco['id']}, Nombre: {disco['nombre']}, Artista: {disco['Artista']}, Género: {disco['Genero']}, Cantidad: {disco['cantidad']}")
        
    else:
        print('No se encontraron discos disponibles.')
        return 0
    
def retirar_Disco(idaretirar,diccionariodiscos):
    id_encontrado=False
    while not id_encontrado:
        
        control=False
        
        for i in diccionariodiscos: #Busamos el id ingresado por el usuario dentro del stock 
            if i["id"]==idaretirar:
                diccionarioamodificar=diccionariodiscos[idaretirar-1]
                diccionarioamodificar["cantidad"]-=1
                print("stock actualizado")
                control=True
        
        if control:
            id_encontrado=True
            return diccionarioamodificar["nombre"]

        else:        
            idaretirar=int(input("Ingrese el id del disco que desea retirar"))
   
    
    print(f"Este es el nuevo stock del disco {diccionarioamodificar}")

def agregar_Disco(nombrealbum,diccionariodiscos):
    for disco in diccionariodiscos:
        if nombrealbum== disco['nombre']:
            disco['cantidad'] += 1

 