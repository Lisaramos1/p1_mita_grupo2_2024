import DiscosStock
import prestamos
import Personas
import funcionesvarias

discos = {
    {'id':1,'nombre':'Disco 1','Artista':"A",'Genero':'Rock','cantidad':5},
    {'id':2,'nombre':'Disco 2','Artista':"B",'Genero':'Pop','cantidad':3},
    {'id':3,'nombre':'Disco 3','Artista':"C",'Genero':'Techno','cantidad':2},
    {'id':4,'nombre':'Disco 4','Artista':"D",'Genero':'Dubstep','cantidad':7},
    {'id':5,'nombre':'Disco 5','Artista':"E",'Genero':'Rock nacional','cantidad':1},
    {'id':6,'nombre':'Disco 6','Artista':"F",'Genero':'Rock cristiano alternativo','cantidad':4},
    {'id':7,'nombre':'Disco 7','Artista':"G",'Genero':'Trap','cantidad':6},
    {'id':8,'nombre':'Disco 8','Artista':"H",'Genero':'Cumbia','cantidad':2},
    {'id':9,'nombre':'Disco 9','Artista':"I",'Genero':'Indie','cantidad':8},
    {'id':10,'nombre':'Disco 10','Artista':"J",'Genero':'Clasica','cantidad':3}
}

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
            
            loopfiltro=0  #Se llama a la funcion para verificar la disponibilidad del album
            while loopfiltro == 0 : 
                print('1 Id del disco ')
                print('2 Nombre del disco ')
                print('3 Nombre del artista ')
                print('4 Genero del album ')
                print()
                indicefiltro=int(input("Ingrese como desea buscar el album: "))
                if indicefiltro > 4 or indicefiltro< 1:
                    print("Ingrese un numero valido")   
                else:
                    loopfiltro=1
            
            valorabuscar=input("Ingrese el valor a buscar: ")
            idalbum=funcionesvarias.disponibilidadalbum(indicefiltro,valorabuscar,discos)
            Diasdeprestamos=int(input("Ingrese cuantos dias se realizara el prestamo: "))
            prestamos.crear_prestamos(NroCliente,idalbum,Diasdeprestamos)
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
