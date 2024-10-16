
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

def modificaralbum(diccionario,tupladediccionario,nuevovalor):
    menu_busqueda_album(diccionario,tupladediccionario)
    

#busquedas de albums
def menu_busqueda_album(diccionario, tupladediccionarios):
    
    """
    Se inician los filtros de busqueda , se envian los parametros para realizar la busqueda de albums
    estructura de la tupla:(nombre_disco,nombre_artista,genero)
    """
    print('1 Id del disco ')
    print('2 Nombre del disco ')
    print('3 Nombre del artista ')
    print('4 Genero del album ')
    print()
    
    
    while True: #Manejo de errores
        try: 
            indice=int(input("Ingrese por cual valor desea realizar la busqueda:"))
            break
        except (ValueError):
            print("Debe ingresar un valor entero")
    
    
    match indice:
        case 1 :
            busqueda=(int(input("Ingrese el id que desea buscar: ")))
            valores=busquedaporvalores(diccionario,None,busqueda)
        case 2:
            busqueda=(input("Ingrese el nombre del disco que desea buscar: "))
            valores=busquedaporvalores(diccionario,tupladediccionarios[0],busqueda)
        case 3:
            busqueda=(input("Ingrese el nombre del artista del disco que desea buscar: "))
            valores=busquedaporvalores(diccionario,tupladediccionarios[1],busqueda)
        case 4:
            busqueda=(input("Ingrese el genero del disco que desea buscar: "))
            valores=busquedaporvalores(diccionario,tupladediccionarios[2],busqueda)

def busquedaporvalores(diccionario,subdiccionario, valorbuscar):
    """
    Se realiza la busqueda por albums , dentro de los subdiccionarios de ids
    """
    
    if subdiccionario==None: #Se concoce el id del disco por lo cual la busqueda es directa al dic. principal
        if valorbuscar in diccionario:
            print(f"{valorbuscar}{diccionario.get(valorbuscar)}")
        else:
            print("El disco no fue encontrado")    
   
    else :
        iddiscosabuscar=subdiccionario.get(valorbuscar.lower(),None)
        if iddiscosabuscar!=None:
            print([(album_id,diccionario[album_id]) for album_id in iddiscosabuscar]) #Se itera dentro de la lista con los id de los discos , y se agregan a la nueva lista con los valores completos del dict. principal
        else:
            print("La caracteristica no fue encontrada")

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

 