import DiscosStock
import prestamos
import Personas
uso=0
while uso==0:
    print('1 Discos')
    print('2 Usuarios')
    print('3 Prestamos')
    print('0 Salir')
    funcion = int(input())
    if funcion==1:
        loop=0
        while loop==0:
            print('ingrese un numero del 0 al 4')
            print('1: Agregar Discos ➕')
            print('2: Modificar Discos ⚙')
            print('3: Eliminar Discos ✖')
            print('4: Ver Stock 👀')
            print('0: Volver')
            menu = int(input())
            if menu==1:
                DiscosStock.agregar()
            elif menu==2:
                DiscosStock.modificar()
            elif menu==3:
                DiscosStock.eliminar()
            elif menu==4:
                DiscosStock.mostrar()
            elif menu==0:
                loop=1
    elif funcion==2:
        Personas.menue()
    if funcion==3:
        loop=0
    while loop == 0 :
        print('1 Crear prestamos ➕')
        print('2 Modificar prestamos ➖')
        print('3 Eliminar prestamo ⚙️')
        print('4 Mostrar listado 👀')
        print('5 Devoluciones')
        print("0 volver")
        menu = int(input('Ingrese una acción:' ))
        if menu==1:
            NroCliente=int(input("Ingrese el numero de cliente: ")) 
            Album=input("Ingrese el nombre del album: ")
            Diasdeprestamos=int(input("Ingrese cuantos dias se realizara el prestamo: "))
            prestamos.crear_prestamos(NroCliente,Album,Diasdeprestamos)
        if menu==2:
            userid=int(input("Ingrese el id del usuario del registro a modificar: "))
            prestamos.modificar_prestamos(userid) 
        if menu==3:
            prestamos.eliminar_prestamos()
        if menu==4:
            prestamos.mostrar_prestamos()
        if menu == 5:
            print('1 Devolver un disco ➕')
            print('2 Modificar la devolucion ➖')
            print('4 Mostrar estados de los prestamos 👀')
            print('5 Devoluciones')
            print("0 volver")
            
        if menu == 0:
            loop=1
        else : 
            print("Ingrese un numero valido")
        
    else:
        uso=1
