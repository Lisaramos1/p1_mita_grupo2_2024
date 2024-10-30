import json
    
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
def menu_busqueda_album(db_discos):
    
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
            continue
        
        if indicefiltro > 4 or indicefiltro< 1:
            print("Ingrese un numero valido")
        else: 
            break
    
    #apertura del archivo con todos los discos    
    try: 
        with open(db_discos,"r",encoding="UFT-8") as datos:
            diccionario=json.load(datos)
    except:
        print("No se pudo abrir el archivo")
        
    while True:
       
        match indice:
            case 1 :
                busqueda=((input("Ingrese el id que desea buscar: ")))
                valores=busquedaporvalores(diccionario,None,busqueda)
            case 2:
                busqueda=(input("Ingrese el nombre del disco que desea buscar: "))
                try :
                    archivo=open("nombre_album.json","r")
                except :
                    print("No se puede abrir el archivo")
                else:
                    nombres_album=json.load(archivo)
                    valores=busquedaporvalores(diccionario,nombres_album,busqueda)
                finally:
                    archivo.close()
            case 3:
                busqueda=(input("Ingrese el nombre del artista del disco que desea buscar: "))
                try :
                    archivo=open("artistas.json","r")
                except :
                    print("No se puede abrir el archivo")
                else:
                    artistas=json.load(archivo)
                    valores=busquedaporvalores(diccionario,artistas,busqueda)
                finally:
                    archivo.close()
            case 4:
                busqueda=(input("Ingrese el genero del disco que desea buscar: "))
                try :
                    archivo=open("generos.json","r")
                except :
                    print("No se puede abrir el archivo")
                else:
                    generos=json.load(archivo)
                    valores=busquedaporvalores(diccionario,generos,busqueda)
                finally:
                    archivo.close()  #Llamada de la funcion dentro de otra funcción
        if valores==False:
            continue
        else :
            break
        
def busquedaporvalores(diccionario,subdiccionario, valorbuscar):
    """
    Se realiza la busqueda por albums , dentro de los subdiccionarios de ids
    """
    
    
    if subdiccionario==None: #Se concoce el id del disco por lo cual la busqueda es directa al dic. principal
        if valorbuscar in diccionario:
            print(f"{valorbuscar}{diccionario.get(valorbuscar)}")
            return True
        else:
            print("El disco no fue encontrado")
            return False    
   
    else :
        print(subdiccionario)
        iddiscosabuscar=subdiccionario.get(valorbuscar.lower(),None)
        if iddiscosabuscar!=None:
            aux=([(album_id,diccionario[album_id]) for album_id in iddiscosabuscar]) #Se itera dentro del conjunto con los id de los discos , y se agregan a la nueva lista con los valores completos del dict. principal
            imprimir_matriz(aux)
            return True
        else:
            print("La caracteristica no fue encontrada")
            return False

def retirar_Disco(idaretirar,diccionariodiscos):
    
    if idaretirar not in diccionariodiscos:
        assert KeyError,("El disco no fue encontrado")
    
        
    elif idaretirar in diccionariodiscos:
        idaretirar["cantidad"]-=1
        print("Stock actulizado \n")
        print(diccionariodiscos.values(idaretirar))
        
        
    elif idaretirar["cantidad"]==0:
        print("El disco no se encuentra disponible")
        
    

def agregar_Disco(nombrealbum,diccionariodiscos):
    for disco in diccionariodiscos:
        if nombrealbum== disco['nombre']:
            disco['cantidad'] += 1

 