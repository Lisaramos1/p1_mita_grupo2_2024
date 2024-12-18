import validaciones 
import Personas
import funcionesvarias
from datetime  import datetime
import json
import DiscosStock




def crear_prestamos (NroCliente,album,iddisco,DiasdePrestamo,monto,Db_prestamos):
    """
    Recibe los inputs para asignarlo a un nuevo prestamo de la matriz
    """
    fechas=validaciones.SumadeDias(DiasdePrestamo)       #Se contabilizan las fechas de los dias del prestamos
    fecha_inicio,fecha_cierre=fechas                     # Se asignan las fechas
    aux=f"{NroCliente},{album},{iddisco},{fecha_inicio},{fecha_cierre},{monto},{"False"}"
    print(f"El prestamo creado es: {aux}")
    
    try :
        with open (Db_prestamos,"a",encoding="utf-8") as ultima_linea:
            ultima_linea.write(aux+ "\n")
    except FileNotFoundError:
        print(f"no se pudo abrir el archivo {Db_prestamos}")
    else:
        print("Base de datos actualizada...") 

def mostrar_prestamos(Prestamos_db):
    encabezado=["userid","disco","discoid","inicio","cierre","monto","estado"]
    espacios=[8,20,10,15,15,11,7]
    fila=""
    for i , valor in enumerate(encabezado):
        fila += f"{valor:<{espacios[i]}}"
    print()
    print(fila)
    print("-"*sum(espacios))
    
    try:
        with open(Prestamos_db,"r",encoding="utf-8")as data:
            for linea in data:
                datos=linea.strip().split(",")
                fila=""
                for i , j in enumerate(datos):
                    if i == 1:  
                        j = j[:15] 
                    fila += f"{j:<{espacios[i]}}"
                print(fila)
    except:
        print("Ocurrio un error con el archivo")     
        return
    finally:
        print("-"*(sum(espacios)+len(encabezado)),"\n")

def actualizar_txt(prestamostxt,prestamoamodificar,n_aparicion,modificacion):
    try: #Realizamos un backup de la matriz sin los datos que se modificaron anteriormente
        with open(prestamostxt, "r", encoding="utf-8") as data:
            with open("Db/prestamos_db_backup.txt", "w", encoding="utf-8") as backup:
                cont=0
                for linea in data:
                    if not linea: pass
                    
                    if cont == int(n_aparicion) and modificacion==True:
                        if prestamoamodificar.strip() != "":
                            backup.write(prestamoamodificar + "\n")
                    else:
                        backup.write(linea)
                    cont+=1

    except FileNotFoundError:
        print("No se encontro el archivo")

    try: #Actualizamos a partir del backup
        with open("Db/prestamos_db_backup.txt", "r", encoding="utf-8") as backup:
            with open(prestamostxt, "w", encoding="utf-8") as data:
                for linea in backup:
                    data.write(linea)   
                         
    except FileNotFoundError:
        print("No se encontro el archivo")

    print(f"\n Listado actulizado... \n")
    

def busqueda_prestamos(userid,prestamostxt,estadoprestamo):
    """
    pre:Recibe el id a buscar y el archico donde se encuentran los prestamos
    pos:Regresa un diccionario con las apariciones de los prestamos, con indice de la matrix de prestamos
    """
    apariciones={}
    try: 
        nro_linea=0
        arch=open (prestamostxt , "r", encoding="utf-8")
        linea=arch.readline()
        while linea:
            listavalores=user,disco,iddisco,fechaini,fechedevo,monto,estado=linea.strip().split(",")
            
            if (user)==userid and estadoprestamo=='False' and estado=="False": #Solo filtra por los prestamos que no han sido devueltos
                apariciones.setdefault(str(nro_linea),listavalores)
                
            elif (user)==userid and estadoprestamo==True:  
                apariciones.setdefault(str(nro_linea),listavalores)
            linea=arch.readline()
            nro_linea+=1
                
                
    except FileNotFoundError:
        print(f"El archivo {prestamostxt} no se pudo abrir")
        
    finally:
        arch.close()
        if len(apariciones)>0:
            funcionesvarias.imprimir_diccionario(apariciones)
            return apariciones
        else:
            return False
    
    
def modificar_prestamos(userid,usersjson,prestamostxt,discosjson):
        
              
    apariciones=busqueda_prestamos(userid,prestamostxt,True)
            
    print()
              
    n_aparicion=(input("Qué prestamo desea modificar? "))
    
    prestamoacambiar=apariciones[n_aparicion]
    print((prestamoacambiar))
    print('1 Numero de cliente')
    print('2 Nombre del album')
    print('3 Fecha de prestamo')
    print('4 Fecha de finalización de prestamo')
    print('5 Monto')
    print()
    
    while True :
        try:
            modificacion=int(input("Que valor desea modificar?:"))-1
        except ValueError:
            print("El valor debe ser un número")
            continue
        if modificacion >= len(prestamoacambiar)or modificacion<0:
            print("El valor ingresado no es correcto")
        else :
            break
        
    control=True    
    while control==True :
        match modificacion:
            case 0:#Modificación de numero de cliente 
                idcliente=input("Ingrese el nuevo id de cliente")
                caso1=validaciones.ValidUserid(idcliente) # En caso que la estructura del id no sea la correcta
                while caso1 == False:
                    print(f"El numero de usuario {idcliente} , no cumple con los parametros")

                caso2=validaciones.existenciadeuser(idcliente,usersjson) #Caso en que el usuario no esta registrado
                while caso2==False:
                    print(f"El usuario {userid} , no esta registrado")
                    idcliente=input("Ingrese un Id registrado : ")
                    caso2=validaciones.existenciadeuser(idcliente,usersjson) #Caso en que el usuario no esta registrado


                prestamoacambiar[modificacion]=idcliente

            case 1 :
                loopfiltro=0  
                print("Busqueda de album")
                discosencontrados=funcionesvarias.menu_busqueda_album(discosjson)

                if len(discosencontrados)==1:
                    aux=list(discosencontrados.keys())
                    idnuevodisco=aux[0]
                else:
                    idnuevodisco=input("Que disco desea retirar? ")


                funcionesvarias.retirar_Disco(discosjson,idnuevodisco)
                nombrealbum=discosencontrados[idnuevodisco]["nombre".lower()]
                aux=prestamoacambiar[modificacion]
                prestamoacambiar[modificacion]=nombrealbum
                iddisco=prestamoacambiar[3]
                #Se agrega el disco devuelto a stock
                disco=DiscosStock.cargar_disco()
                disco[str(iddisco)]['cantidad']+=1
                DiscosStock.guardar_disco(disco)


            case 2: #Cambio de fecha de inicio de prestamo
                print("Ingrese la nueva fecha con el siguiente formato: año-mes-dia")
                nuevafecha=input()
                caso1=validaciones.validaciondefecha(nuevafecha)
                while caso1== False:
                    print("El formato de fecha no es el correcto")
                    print("xxxx-xx-xx")   
                    nuevafecha=input()
                    caso1=validaciones.validaciondefecha(nuevafecha)

                aux=validaciones.str_a_fecha(nuevafecha)
                prestamoacambiar[modificacion]=str(aux)

            case 3: #Cambio de fecha de devolución
                fechaanterior=prestamoacambiar[modificacion] 
                cantdias=int(input("Ingrese la cantidad de días que se le van a sumar al prestamo: "))
                nuevafecha=validaciones.modificacionfechalimite(fechaanterior,cantdias)

                while nuevafecha == False:
                    print("Cantidad de días no valida")
                    cantdias=int(input("Ingrese una cantidad de días mayor que cero: "))
                    nuevafecha=validaciones.modificacionfechalimite(fechaanterior,cantdias)

                prestamoacambiar[modificacion]=nuevafecha

            case 4:#Modificar el monto del prestamo
                nuevo_valor=int(input("Ingrese el nuevo monto del prestamo"))
                prestamoacambiar[modificacion]=str(nuevo_valor)
            
        

        print(f"listado actualizado {prestamoacambiar}" )   
        modificacion=int(input("Que valor desea modificar? Si ya finalizo todas las modificaciones ingrese -1: "))-1
        if modificacion == -2:
            control=False

    
    formatostr= ",".join(prestamoacambiar)
    actualizar_txt(prestamostxt,formatostr,n_aparicion,True)
   
    mostrar_prestamos(prestamostxt) 
        
           
            
   

def eliminar_prestamos(userid,prestamostxt):
    print("\n Eliminación de prestamos")
    apariciones=busqueda_prestamos(userid,prestamostxt,True)

    if apariciones== False:
        return
    else:
        n_aparicion=(input("Qué prestamo desea eliminar? "))
        prestamo_a_eliminar=apariciones[n_aparicion]
        print("\n Este es el prestamo que se eliminara:")
        print((prestamo_a_eliminar))
        formatostr=",".join(prestamo_a_eliminar)
        actualizar_txt(prestamostxt," ",n_aparicion,True)

def prestamos_vencidos(fechalimite,prestamostxt): #Listas por comprensión
    """
    pre:Recibe la fecha por la cual se quiere filtrar y la matriz de prestamos.
    fecha limite:str
    prestamostxt:str
    
    
    """ 
    print("Filtrando\n")
    prestamos_activos=[]
    try:  
        with open(prestamostxt,"r",encoding="utf-8") as archivo:
            linea=archivo.readline() 
            fechalimite=validaciones.str_a_fecha(fechalimite)
            while linea:
                prestamo=linea.strip().split(",")
                if prestamo[-1]=='False':
                    prestamo[4]=validaciones.str_a_fecha(prestamo[3])
                    prestamos_activos.append(prestamo)
                    
                    
                    
                linea=archivo.readline() 
                
        listadeprestamosv = [prestamo for prestamo in prestamos_activos if prestamo[4] > fechalimite]
    
        listadeprestamosv= list(map(lambda prestamo: [*prestamo[:4], prestamo[4].strftime("%Y-%m-%d"), *prestamo[5:]], listadeprestamosv))
        funcionesvarias.imprimir_matriz(listadeprestamosv)
    
    except:
        print("Ha ocurrido un error")
    