import validaciones 
import Personas
import funcionesvarias
from datetime  import datetime



def crear_prestamos (NroCliente,album,DiasdePrestamo,monto,matrizprestamos):
    """
    Recibe los inputs para asignarlo a un nuevo prestamo de la matriz
    """
   
    print("Creación de prestamos") 
    fechas=validaciones.SumadeDias(DiasdePrestamo)       #Se contabilizan las fechas de los dias del prestamos
    fecha_inicio,fecha_cierre=fechas                     # Se asignan las fechas
    aux=[NroCliente,album,fecha_inicio,fecha_cierre,monto,False]
    matrizprestamos.append(aux)
    print(f"El prestamo creado es: {aux}")
    return 


def modificar_prestamos(userid,diccionariousers,matrizprestamos,diccionariodiscos):    
    apariciones,indicedeprestamo=[],[]
 
    verificacion=validaciones.ValidUserid(userid) #Se verifica que el id sea valido
    if verificacion==False:
        print(f"El numero de usuario {userid} , no es valido")
        return

    filas=len(matrizprestamos)
     
    for num in range (filas): # Se verifica que el usuario tenga un prestamo 
        if matrizprestamos[num][0]==userid:
            apariciones.append(matrizprestamos[num])
            indicedeprestamo.append(num)
    
            
    print()
    if len(apariciones)!=0:
        for i in range (len(apariciones)): #Se imprimen las apareciones dentro de prestamos
            print(f'{i+1}- {"%3s" % apariciones[i][1:7]}') #slicing

                  
        n_aparicion=int(input("Qué prestamo desea modificar? "))-1
        
        prestamoacambiar=apariciones[n_aparicion]
        print(str(prestamoacambiar))
        print('1 Numero de cliente')
        print('2 Nombre del album')
        print('3 Fecha de prestamo')
        print('4 Fecha de finalización de prestamo')
        print('5 Monto')
        
        
        
        modificacion=int(input("Que valor desea modificar?: "))-1
        
        while modificacion!=-2:
            if modificacion >= len(prestamoacambiar): #Aseguramos que este dentro del rango el indice 
                print('No es un rango disponible')
            
            if modificacion==0:#Modificación de numero de cliente
                idcliente=input("Ingrese el nuevo id de cliente")
                caso1=validaciones.ValidUserid(idcliente)
                while caso1 == False:
                    print(f"El numero de usuario {idcliente} , no cumple con los parametros")
                    
                caso2=validaciones.existenciadeuser(idcliente,diccionariousers)
                while verificacion==False:
                    print(f"El usuario {userid} , no esta registrado")
                    idcliente=input("Ingrese un Id registrado : ")
                    
                   
                prestamoacambiar[modificacion]=idcliente
            
            elif modificacion == 1 :
                loopfiltro=0  #Se llama a la funcion para verificar la disponibilidad del album
                print()
                print("Busqueda de album")
                while loopfiltro == 0 : 
                    funcionesvarias.menu_busqueda_album()
                    indicefiltro=int(input("Ingrese como desea buscar el album: "))
                    if indicefiltro > 4 or indicefiltro< 1:
                        print("Ingrese un numero valido")   
                    else:
                        loopfiltro=1
                        
                valorabuscar=input("Ingrese el valor a buscar: ")
                funcionesvarias.filtros_busqueda(indicefiltro,valorabuscar,diccionariodiscos)
                
                id=int(input("Ingrese el id del disco que desea retirar: "))
                while id < 0 :
                    id=int(input("Ingrese un numero de id valido: "))
                    
                aux=prestamoacambiar[modificacion]
                nombrealbum=funcionesvarias.retirar_Disco(id,diccionariodiscos)
                prestamoacambiar[modificacion]=nombrealbum
                funcionesvarias.agregar_Disco(aux,diccionariodiscos)
               
                
                
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
        
        matrizprestamos.pop(indicedeprestamo[n_aparicion])    #listas avanzadas
        matrizprestamos.insert(indicedeprestamo[n_aparicion],prestamoacambiar)
        
        print()
        funcionesvarias.imprimir_matriz(matrizprestamos) 
        
    else:
        print("No se encontro ningun prestamo con este numero de usuario")
    return       
            
def mostrar_prestamos(matrizprestamos):
    funcionesvarias.imprimir_matriz(matrizprestamos) 
    return    

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