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

def imprimir_diccionario(diccionario):
    for key, value in diccionario.items():
        print(f"{key:<4}-{value}")

#busquedas de albums
def menu_busqueda_album(db_discos):

    """
    pre :Se inician los filtros de busqueda , se envian los parametros para realizar la busqueda de albums
    pos: Se imprimen en consola los ids coincidentes , se regresa el nombre del album elegido 

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
            False
    
    #apertura del archivo con todos los discos    
    try: 
        with open(db_discos,"r",encoding="UTF-8") as datos:
            diccionario=json.load(datos)
    except:
        return print(f"No se pudo abrir el archivo {db_discos}")
        
    
        
    while True:
       
        match indice:
            case 1 :
                busqueda=((input("Ingrese el id que desea buscar: ")))
                valores=busquedaporvalores(diccionario,None,busqueda)
            
            #Busqueda por por indice invertido , se llama a la funcion para cargar el subddicionario para la busqueda
            case 2:
                busqueda=(input("Ingrese el nombre del disco que desea buscar: "))
                valores = cargar_y_buscar("Db/nombre_album.json",diccionario,busqueda)
            case 3:
                busqueda=(input("Ingrese el nombre del artista del disco que desea buscar: "))
                valores = cargar_y_buscar("Db/artistas.json",diccionario,busqueda)
                
            case 4:
                busqueda=(input("Ingrese el genero del disco que desea buscar: "))
                valores = cargar_y_buscar("Db/generos.json",diccionario,busqueda)
                 
                    
        if valores==False:
            continue #Continuamos haciendo el llamado hasta encontrar el valor buscado
        else :
            return valores #Todos los valores encontrados , en un diccionario , para tener los datos en main
            break  #Fin de la busqueda

def cargar_y_buscar(nombre_archivo,diccionario,busqueda):
    """
     pre :se serializa el subddiccionario elegido en una variable 
     pos : se hace el llamado a la busqueda en el diccionario principal ya cargado
    """
    try:
        with open(nombre_archivo,"r",encoding="UTF-8") as archivo:
            subdiccionario=json.load(archivo)
            return busquedaporvalores(diccionario,subdiccionario,busqueda)
    except:
        print(f"No se pudo abrir el archivo {nombre_archivo}")
        return False
        
def busquedaporvalores(diccionario,subdiccionario, valorbuscar):
    
    """
    Se realiza la busqueda por albums , dentro de los subdiccionarios de ids
    """
    
    
    if subdiccionario==None:    #Se concoce el id del disco por lo cual la busqueda es directa al dic. principal
        if valorbuscar in diccionario:
            print(f"{valorbuscar}-{diccionario.get(valorbuscar)}")
            aux={valorbuscar:diccionario.get(valorbuscar)}
            
            
            if aux[valorbuscar]["Cantidad".lower()]<=0:
                print ("No hay disponibilidad del disco solicitado")
                return False    
        
            return aux
            
        else:
            print("El disco no fue encontrado")
            return False    

    else:
        print(f"\n**SUBDICCIONARIO**\n")
        imprimir_diccionario(subdiccionario)
        
        
        iddiscosabuscar = subdiccionario.get(valorbuscar.lower(), None)
        
        if iddiscosabuscar is not None:
            print("imprimiendo resultados encontrados...\n")
            aux ={album_id: diccionario[album_id] for album_id in iddiscosabuscar if album_id in diccionario and diccionario[album_id]["cantidad"]>0}
            imprimir_diccionario(aux)
            return aux
            
        else:
            print(f"La característica '{valorbuscar}' no fue encontrada")
            return False

def retirar_Disco(db_discos,idaretirar):
    
    try:  
        with open(db_discos,"r",encoding="UTF-8") as datos:
            diccionario=json.load(datos) # serialización de json a objeto de db de discos 
            
        with open("Db/discos_backup.json", "w", encoding="UTF-8") as backup:
            json.dump(diccionario, backup,ensure_ascii=False,indent=4) #Creacion del backup
            
            
    except:
        print("No se pudo abrir el archivo")
    
    
    if idaretirar not in diccionario:
        assert KeyError,("El disco no fue encontrado")
    
    else:    
        if idaretirar in diccionario:
            diccionario[idaretirar]["cantidad"]-=1
            print("Stock actulizado")
            print(f"La nueva cantidad de discos es de {diccionario[idaretirar]["cantidad"]} \n ")
            
        
        
        elif diccionario[idaretirar]["cantidad"]==0:
            print("El disco no se encuentra disponible")
    
    try : 
        with open(db_discos , "w" , encoding="UTF-8")as archivo: #Se cargan los cambios a la db json  
            json.dump(diccionario,archivo,ensure_ascii=False,indent=4)
            
        with open("Db/discos.ndjson", "w", encoding="UTF-8") as archivo_ndjson: #Creamos el archivo ndjson / Posterior uso en Recursividad
            for key, disco in diccionario.items():
                json.dump(disco,archivo_ndjson,ensure_ascii=False)
                archivo_ndjson.write("\n")
    except FileNotFoundError :
        print("m")
    
    
    
 
def agregar_Disco(db_discos,id_disco_nuevo):
    
    try:  
        with open(db_discos,"r",encoding="UTF-8") as datos:
            diccionario=json.load(datos) # serialización de json a objeto de db de discos 
            
        with open("Db/discos_backup.json", "w", encoding="UTF-8") as backup:
            json.dump(diccionario, backup,ensure_ascii=False,indent=4) #Creacion del backup
                    
    except:
        print("No se pudo abrir el archivo")



def suma_cantidad_discos(discos_db,total=0):
    
    linea=discos_db.readline()
    if not linea:
        return total
    
    
    try:
        disco=json.loads(linea.strip())
        total+=disco["cantidad"]
    except:
        pass
        
    
    return suma_cantidad_discos(discos_db,total)


