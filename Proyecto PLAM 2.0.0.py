import DiscosStock
import prestamos
import Personas
import funcionesvarias
import validaciones
import devoluciones

discos = {
    1:{'nombre':'Disco 1','Artista':"A",'Genero':'Rock','cantidad':5},
    2:{'nombre':'Disco 2','Artista':"B",'Genero':'Pop','cantidad':3},
    3:{'nombre':'Disco 3','Artista':"C",'Genero':'Techno','cantidad':2},
    4:{'nombre':'Disco 4','Artista':"D",'Genero':'Dubstep','cantidad':7},
    5:{'nombre':'Disco 5','Artista':"E",'Genero':'Rock nacional','cantidad':1},
    6:{'nombre':'Disco 6','Artista':"F",'Genero':'Rock cristiano alternativo','cantidad':4},
    7:{'nombre':'Disco 7','Artista':"G",'Genero':'Trap','cantidad':6},
    8:{'nombre':'Disco 8','Artista':"H",'Genero':'Cumbia','cantidad':2},
    9:{'nombre':'Disco 9','Artista':"I",'Genero':'Indie','cantidad':8},
    10:{'nombre':'Disco 10','Artista':"J",'Genero':'Clasica','cantidad':3}
}

Usuarios={
    "0001":{"nombre": "Juan", "apellido": "Perez", "dni": "12345678"},
    "0002":{"nombre": "Ana", "apellido": "Gomez", "dni": "23456789"},
    "0003":{"nombre": "Luis", "apellido": "Martinez", "dni": "34567890"},
    "0004":{"nombre": "Maria", "apellido": "Lopez", "dni": "45678901"},
    "0005":{"nombre": "Carlos", "apellido": "Sanchez", "dni": "56789012"}
}

#Matrices
Prestamos=[
    ["0001", 'Disco 1', "2024-06-16", '2024-06-30', 400, False],
    ["0001", 'Disco 4', '2024-06-13', '2024-07-14', 700, False],
    ["0004", 'Disco 6', '2024-06-14', '2024-08-16', 1000, True],
    ["0005", 'Disco 4', '2024-06-14', '2024-08-16', 1000, True]
]
uso=0
while uso==0:
    print('1 Discos')
    print('2 Usuarios')
    print('3 Prestamos')
    print('4 Devoluciones')
    print('0 Salir')
    funcion = int(input("Ingrese que función quiere realizar: "))
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
                discos = DiscosStock.agregar(discos)
            elif menu==2:
                discos = DiscosStock.modificar(discos)
            elif menu==3:
                discos = DiscosStock.eliminar(discos)
            elif menu==4:
                discos = DiscosStock.mostrar(discos)
            elif menu==0:
                loop=1
            else:
                print('Opcion no valida')
    elif funcion==2:
        Personas.menue(Usuarios)
    elif funcion==3:
        loop_prestamos=0
        while loop_prestamos== 0 :
            print()
            print('1 Crear prestamos ➕')
            print('2 Modificar prestamos ➖')
            print('3 Eliminar prestamo ⚙️')
            print('4 Mostrar listado 👀')
            print('5 Prestamos por vencer')
            print("0 volver")
            menu_prestamos = int(input('Ingrese una acción:' ))
            
            if menu_prestamos==1:
                
                control=True #variable para controlar la carga del usuario
                while control==True:
                    NroCliente=(input("Ingrese el numero de cliente: "))
                    verificacionuserid=validaciones.ValidUserid(NroCliente) #Se verifica que el user cargado coincida con el parametro regex.
                    while verificacionuserid == False:
                        print("Nro de cliente no valido")
                        NroCliente=(input("Ingrese un numero de cliente valido: "))
                        verificacionuserid=validaciones.ValidUserid(NroCliente)
                    
                    user=validaciones.existenciadeuser(NroCliente,Usuarios) #Validacion de existencia del usuario
                    if user == True:
                        print("Cliente encontrado")
                
                    else:
                        print("El usuario no fue encontrado")  #Si el usuario no esta registrado regresa al menu principal 
                        print("Debe restrirar al usuario")
                        control=False
                        break  
                        
                        
                    loopfiltro=0  #Se llama a la funcion para verificar la disponibilidad del album
                    print()
                    funcionesvarias.menu_busqueda_album()
                    print("Busqueda de album")
                    while loopfiltro == 0 : 
                        funcionesvarias.menu_busqueda_album
                        indicefiltro=int(input("Ingrese como desea buscar el album: "))
                        if indicefiltro > 4 or indicefiltro< 1:
                            0("Ingrese un numero valido")   
                        else:
                            loopfiltro=1
                            
                    valorabuscar=input("Ingrese el valor a buscar: ")
                    funcionesvarias.filtros_busqueda(indicefiltro,valorabuscar,discos)
                    nombredelalbum=funcionesvarias.retirar_Disco(id,discos)
                    if nombredelalbum == 0 : 
                        break
        
                    Diasdeprestamos=int(input("Ingrese cuantos dias se realizara el prestamo: "))
                    monto=int(input("Ingrese el monto total del prestamo: "))
                    prestamos.crear_prestamos(NroCliente,nombredelalbum,Diasdeprestamos,monto,Prestamos)
                    control=False 
                    
            if menu_prestamos==2:
                print()
                print("Modificación de prestamos \n")
                userid=(input("Ingrese el id del usuario del registro a modificar: "))
                prestamos.modificar_prestamos(userid,Personas,Prestamos,discos)
            if menu_prestamos==3:
                prestamos.eliminar_prestamos(Prestamos)
            if menu_prestamos==4:
                prestamos.mostrar_prestamos(Prestamos)
            if menu_prestamos==5:
                fechalimite=input("Ingrese la fecha limite que desea filtrar: ")
                caso1=validaciones.validaciondefecha(fechalimite)
                while caso1== False: #Se evalua que sea correcto el formato de fecha
                    print("El formato de fecha no es el correcto")
                    print("xxxx-xx-xx")   
                    fechalimite=input()
                    caso1=validaciones.validaciondefecha(fechalimite)
                prestamos.prestamos_vencidos(fechalimite,Prestamos)
                
                
                
            if menu_prestamos == 0:
                loop_prestamos=1
    
    elif funcion==4:
        loop_devoluciones=0
        while loop_devoluciones==0:
            print('1 Devolver un disco ➕')
            print("0 volver")
            menu_devoluciones = int(input('Ingrese una acción:' ))
            
            if menu_devoluciones==1:
            
                print("Devolución de discos \n")
                
                control=False
                while control==False:
                    userid=input("Ingrese el id del usuario: ")
                    verificacionuserid=validaciones.ValidUserid(userid) #Se verifica que el user cargado coincida con el parametro regex.
                    while verificacionuserid == False:
                        print("Nro de cliente no valido")
                        userid=(input("Ingrese un numero de cliente valido: "))
                        verificacionuserid=validaciones.ValidUserid(userid)
                        
                    user=validaciones.existenciaprestamo(userid,Prestamos) #Validacion de existencia de prestamo a nombre del usuario
                    if user == True:
                        print("Prestamo encontrado \n")
    
                
                    else:
                        print("El prestamo no fue encontrado \n")  #Si el usuario no esta registrado regresa al menu principal
                        break
                    
                   
                    
                    
                    loopfiltro=0  
                    print("Busqueda de album")
                    while loopfiltro == 0 : 
                        funcionesvarias.menu_busqueda_album()
                        indicefiltro=int(input("Ingrese como desea buscar el album: "))
                        if indicefiltro > 4 or indicefiltro< 1:
                            print("Ingrese un numero valido")   
                        else:
                            loopfiltro=1
                            
                    valorabuscar=input("Ingrese el valor a buscar: ")
                    funcionesvarias.filtros_busqueda(indicefiltro,valorabuscar,discos)
                    nombredelalbum=input("Ingrese el nombre del album que busca: ")
                    devoluciones.modicacion_de_estados(userid,nombredelalbum,discos,Prestamos)
                    
                    control=True
                
            elif menu_devoluciones==0:
                loop_devoluciones=1
        
    elif funcion ==0 :
        uso=1
    else:
        print('Numero no valido')
