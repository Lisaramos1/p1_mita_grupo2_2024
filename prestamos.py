import validaciones 
import Personas
import funcionesvarias
from datetime  import datetime
import json




def crear_prestamos (NroCliente,album,DiasdePrestamo,monto,Db_prestamos):
    """
    Recibe los inputs para asignarlo a un nuevo prestamo de la matriz
    """
   
    fechas=validaciones.SumadeDias(DiasdePrestamo)       #Se contabilizan las fechas de los dias del prestamos
    fecha_inicio,fecha_cierre=fechas                     # Se asignan las fechas
    aux=f"{NroCliente},{album},{fecha_inicio},{fecha_cierre},{monto},{"False"}"
    print(f"El prestamo creado es: {aux}")
    
    try :
        with open (Db_prestamos,"a",encoding="utf-8") as ultima_linea:
            ultima_linea.write(aux+ "\n")
    except FileNotFoundError:
        print(f"no se pudo abrir el archivo {Db_prestamos}")
    else:
        print("Base de datos actualizada...") 

def mostrar_prestamos(Prestamos_db):
    encabezado=["userid","disco","inicio","cierre","monto","estado"]
    espacios=[10,15,15,15,15,7]
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
                    fila += f"{j:<{espacios[i]}}"
                print(fila)
    except:
        print("Ocurrio un error con el archivo")     
        return
    finally:
        print("-"*sum(espacios),"\n")


def modificar_prestamos(userid,usersjson,prestamostxt,discosjson):    
             
    verificacion=validaciones.ValidUserid(userid) #Se verifica que el id sea valido
    if verificacion==False:
        print(f"El numero de usuario {userid} , no es valido")
        return


    
    apariciones={}
    
    try: 
        nro_linea=0
        arch=open (prestamostxt , "r", encoding="utf-8")
        linea=arch.readline()
        while linea:
            print("Se inicia carga de los prestamos")
            listavalores=user,disco,fechaini,fechedevo,monto,estado=linea.split(",")
            if (user)==userid:
                apariciones.setdefault(str(nro_linea),listavalores)
            linea=arch.readline()
            nro_linea+=1
                
                

    except:
        print(f"El archivo {prestamostxt} no se pudo abrir")
        
    finally:
        arch.close()
        if len(apariciones)>0:
            funcionesvarias.imprimir_diccionario(apariciones)
        else:
            print("Este usuario no presenta ningún prestamo")
            return
    
     
    
    
            
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
    
    
    modificacion=int(input("Que valor desea modificar?:"))-1
    control=True
    while control==True :
        if modificacion >= len(prestamoacambiar): #Aseguramos que este dentro del rango el indice 
            print('No es un rango disponible')
        
        if modificacion==0:#Modificación de numero de cliente
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
        
        elif modificacion == 1 :
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
            #AGREGAR DEVOLUCIÓN A STOCK
            
            
        elif modificacion == 2: #Cambio de fecha de inicio de prestamo
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
                    
        elif modificacion==3: #Cambio de fecha de devolución
            fechaanterior=prestamoacambiar[modificacion] 
            cantdias=int(input("Ingrese la cantidad de días que se le van a sumar al prestamo: "))
            nuevafecha=validaciones.modificacionfechalimite(fechaanterior,cantdias)
            
            while nuevafecha == False:
                print("Cantidad de días no valida")
                cantdias=int(input("Ingrese una cantidad de días mayor que cero: "))
                nuevafecha=validaciones.modificacionfechalimite(fechaanterior,cantdias)
            
            prestamoacambiar[modificacion]=nuevafecha
                
        elif modificacion==4:#Modificar el monto del prestamo
            nuevo_valor=int(input("Ingrese el nuevo monto del prestamo"))
            prestamoacambiar[modificacion]=nuevo_valor
        
        print(f"listado actualizado {prestamoacambiar}")
        
        modificacion=int(input("Que valor desea modificar? Si ya finalizo todas las modificaciones ingrese -1: "))-1
        if modificacion == -2:
            control=False

    
    formatostr=",".join(prestamoacambiar)
    try: #Realizamos un backup de la matriz sin los datos que se modificaron anteriormente
        with open(prestamostxt, "r", encoding="utf-8") as data:
            with open("Db/prestamos_db_backup.txt", "w", encoding="utf-8") as backup:
                cont=0
                for linea in data:
                    if cont == int(n_aparicion):
                        backup.write(formatostr)
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
    mostrar_prestamos(prestamostxt) 
        
           
            
   

def eliminar_prestamos(matrizprestamos):
    for i in range (len(matrizprestamos)): #Se imprimen los prestamos con un indice para poder identificarlos
        print(f'{i+1}- {"%3s" % matrizprestamos[i]}') 
    
    prestamo_a_eliminar=int(input("Que listado desea elimiar? "))-1
    print(f'el prestamo eliminado fue: {matrizprestamos[prestamo_a_eliminar]}')
    print()
    matrizprestamos.pop(prestamo_a_eliminar)
    funcionesvarias.imprimir_matriz(matrizprestamos)
    
    return

def prestamos_vencidos(fechalimite,matrizprestamos): #Listas por comprensión 
    print("Filtrando\n")
    fechalimite_date = datetime.strptime(fechalimite, "%Y-%m-%d")
    
    # Crear la lista auxiliar filtrada
    prestamos_vencidos = [
        prestamo for prestamo in matrizprestamos if not prestamo[-1] and datetime.strptime(prestamo[3], "%Y-%m-%d") < fechalimite_date
    ]
    
    funcionesvarias.imprimir_matriz(prestamos_vencidos)