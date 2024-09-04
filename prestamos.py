import datetime

prestamos=[
    [5002,'Lemonade','12/5', '27/5',400],
    [5003,'Abbey Road','13/6','14/7',700],
    [5007,'Lemonade','14/6','16/8',1000],
    [5007,'Ok Computer','14/6','16/8',1000]
    
]


def crear_prestamos ():
    """
    Recibe los inputs para asignarlo a un nuevo prestamo de la matriz
    """
    print("Creación de prestamos")
    NroCliente=int(input('ingrese el numero del cliente: '))
    
    """
    Verificar si puede retirar un album
    """
    
    Album=input("Ingrese el nombre del album: ")
    
    """
    Disponibilidad
    """
    
    
    fecha_ini=datetime.datetime()
    print(fecha_ini)
    fecha_ciere=input('Ingrese la fecha de cierre del prestamo: ')
    monto=int(input("Ingrese el monto total del prestamo: "))    
    
    aux=[NroCliente,Album,fecha_ini,fecha_ciere,monto]
    prestamos.append(aux)
    return


def modificar_prestamos():    
    apariciones,indicedeprestamo=[],[]
    pku=int(input("Ingrese el id del usuario del registro a modificar: "))
    
    """
    Seleccionar por cual filtro se desea realizar la busqueda 
    """
        
    columnas=len(prestamos[0])-1
    
    # apariciones=[num for num in (prestamos[0]) if prestamos[num] == pku ]      
     
    for num in range (columnas):
        if prestamos[num][0]==pku:
            apariciones.append(prestamos[num])
            indicedeprestamo.append(num)
    
            
    print()
    if len(apariciones)!=0:
        for i in range (len(apariciones)): #Se imprimen las apareciones dentro de prestamos
            print(f'{i+1}- {"%3s" % apariciones[i][1:7]}')

                  
        n_aparicion=int(input("Qué prestamo desea modificar? "))-1
        
        prestamoacambiar=apariciones[n_aparicion]
        print(prestamoacambiar)
        print('1 Numero de cliente')
        print('2 Nombre del album')
        print('3 Fecha de prestamo')
        print('4 Fecha de finalización de prestamo')
        print('5 Monto')
        
        
        
        modificacion=int(input("Que valor desea modificar?: "))-1
        
        while modificacion!=-2:
            if modificacion >= len(prestamoacambiar):
                print('No es un rango disponible')
            
            else:    
                nuevo_valor=input("Ingrese un nuevo valor: ")
                prestamoacambiar[modificacion]=nuevo_valor
            
            print(f"listado actualizado {prestamoacambiar}")
            
            modificacion=int(input("Que valor desea modificar? Si ya finalizo todas las modificaciones ingrese -1: "))-1
        
        prestamos.pop(indicedeprestamo[n_aparicion])     
        prestamos.insert(indicedeprestamo[n_aparicion],prestamoacambiar)
        
        print()
        for i in prestamos:
            print(i)    
        
    else:
        print("No se encontro ningun prestamo")
    return       
            
def mostrar_prestamos():
    for i in prestamos:
        print(i) 
    return    

def eliminar_prestamos():
    for i in range (len(prestamos)): #Se imprimen los prestamos con un indice para poder identificarlos
        print(f'{i+1}- {"%3s" % prestamos[i]}') 
    
    prestamo_a_eliminar=int(input("Que listado desea elimiar? "))-1
    print(f'el prestamo eliminado fue: {prestamos[prestamo_a_eliminar]}')
    print()
    prestamos.pop(prestamo_a_eliminar)
    print(prestamos)
    
    return

def crud_prestamos():
    loop=0
    while loop == 0 :
        print('1 Crear prestamos ➕')
        print('2 Modificar prestamos ➖')
        print('3 Eliminar prestamo ⚙️')
        print('4 Mostrar listado 👀')
        print("0 volver")
        menu = int(input('Ingrese una acción:' ))
        if menu==1:
            crear_prestamos()
        if menu==2:
            modificar_prestamos() 
        if menu==3:
            eliminar_prestamos()
        if menu==4:
            mostrar_prestamos() 
        if menu == 0:
            loop=1
            return
        else : 
            print("Ingrese un numero valido")

