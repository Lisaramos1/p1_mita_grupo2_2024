import validaciones
import Personas

Personas=[
     [5005, 'Juan Perez', 12345678],
    [5006, 'Ana Gomez', 23456789],
    [5007, 'Luis Martinez', 34567890],
    [5008, 'Maria Lopez', 45678901],
    [5009, 'Carlos Sanchez', 56789012]
]

prestamos=[
    [5002,'Lemonade','12/5', '27/5',400,True],
    [5003,'Abbey Road','13/6','14/7',700,False],
    [5007,'Lemonade','14/6','16/8',1000,True],
    [5007,'Ok Computer','14/6','16/8',1000,True]
    
]

aux=validaciones.existenciadeuser(104,prestamos)
print(aux)

def crear_prestamos (NroCliente,album,DiasdePrestamo):
    """
    Recibe los inputs para asignarlo a un nuevo prestamo de la matriz
    """
    
    estado=False
    while estado == False: #While de validaciones
        user=validaciones.existenciadeuser(NroCliente,Personas)
        if user == True:
            print("Existe el nro de cliente")
    
        else:
            print("El usuario no fue encontrado")
            print("Debe restrirar al usuario")
            estado=False
        
        """
        Agregar:
        Disponibilidad del album
        """
        
            
    """
    Agregar:
    Calcular un precio base
    """
    print("Creación de prestamos") 
    fechas=validaciones.SumadeDias(DiasdePrestamo)       #Se contabilizan las fechas de los dias del prestamos
    fecha_inicio,fecha_cierre=fechas                     # Se asignan las fechas
    monto=int(input("Ingrese el monto total del prestamo: "))
    aux=[NroCliente,album,fecha_inicio,fecha_cierre,monto]
    prestamos.append(aux)
    return True


def modificar_prestamos():    
    apariciones,indicedeprestamo=[],[]
    pku=int(input("Ingrese el id del usuario del registro a modificar: "))
    
    """
    AGREGAR:
    Seleccionar por cual filtro se desea realizar la busqueda 
    """
        
    columnas=len(prestamos[0])-1
    
    apariciones=[prestamo for prestamo in prestamos if prestamo[0] == pku ]
    
    """
    Creación de listas por compresión 
    """     
     
    # for num in range (columnas):
    #     if prestamos[num][0]==pku:
    #         apariciones.append(prestamos[num])
    #         indicedeprestamo.append(num)
    
            
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
            NroCliente=int(input("Ingrese el numero de cliente: ")) #Donde debo validar el user id???
            Album=input("Ingrese el nombre del album: ")
            Diasdeprestamos=int(input("Ingrese cuantos dias se realizara el prestamo: "))
            crear_prestamos(NroCliente,Album,Diasdeprestamos)
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

