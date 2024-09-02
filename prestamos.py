
discos=[
    [1000,'Michael Jackson','Billie Jean','Pop'],
    [1001,'The Beatles',"Abbey Road",'Rock'],
    [1002,' Beyoncé','Lemonade','R&B'],
    [1003,'Radiohead', 'Ok Computer' , 'Alternative Rock']
    ]

Clientes= [
    [5000,83745902, "Ana García", "+34 912 345 678", "Calle Mayor 15, Madrid, España"],
    [5001,29873645, "Juan López", "+34 687 234 567", "Avenida de la Constitución 20, Barcelona, España"],
    [5002,56473829, "María Fernández", "+34 954 876 543", "Plaza de España 5, Sevilla, España"],
    [5003,10928374, "Carlos Martínez", "+34 980 543 210", "Gran Vía 10, Valencia, España"],
    [5004,78563412, "Laura Sánchez", "+34 976 123 456", "Calle Real 22, Zaragoza, España"],
    ]

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
    
    fecha_ini=input('ingrese la fecha del prestamo: ')
    fecha_ciere=input('Ingrese la fecha de cierre del prestamo: ')
    monto=int(input("Ingrese el monto total del prestamo: "))    
    
    aux=[NroCliente,Album,fecha_ini,fecha_ciere,monto]
    prestamos.append(aux)


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
    
     
    print(apariciones)
            
    print()
    if len(apariciones)!=0:
        for i in range (len(apariciones)): #Se imprimen las apareciones dentro de prestamos
            print(f'{i+1}- {"%3s" % apariciones[i][1:7]}')

                  
        n_aparicion=int(input("Qué prestamo desea modificar? "))-1
        
        prestamoacambiar=apariciones[1:7]
        print(prestamoacambiar)
        print('1 Numero de cliente')
        print('2 Nombre del album')
        print('3 Fecha de prestamo')
        print('4 Fecha de finalización de prestamo')
        print('5 Monto')
        
        is_modificacion=True
        while is_modificacion==True:
            modificacion=int(input("Que valor desea modificar, si ya finalizo su carga ingrese -1: "))
            if modificacion > len(prestamoacambiar[0]):
                print('No es un rango disponnible')
                modificacion=int(input("Que valor desea modificar?: "))
            is_modificacion=True if modificacion !=-1 else False
            nuevo_valor=input("Ingrese un nuevo valor")
            prestamoacambiar[0][modificacion]=nuevo_valor
            print(prestamoacambiar)
            prestamoacambiar.insert(modificacion,nuevo_valor)
            print(prestamoacambiar)
        prestamos.insert(indicedeprestamo[n_aparicion],prestamoacambiar)
        print(prestamos)    
        
    else:
        print("No se encontro ningun prestamo")
       
            
#def mostrar_prestamos():           
    
def crud_prestamos():
    menu = 0
    while menu == 0 :
        print('1 Crear prestamos')
        print('2 Modificar prestamos')
        print('3 Mostrar listado')
        print('4 Eliminar prestamo ')
        menu = int(input('Ingrese una acción:' ))
        if menu==1:
            crear_prestamos()
        if menu==2:
            modificar_prestamos() 
        if menu==3:
            mostar 
        if menu==4:
            eliminar 

crud_prestamos()