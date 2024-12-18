import DiscosStock
import prestamos
import Personas
import funcionesvarias
import validaciones 
import devoluciones
import json
"""discos={
    "1": {"nombre": "Thriller", "Artista": "Michael Jackson", "Genero": "Pop", "cantidad": 5},
    "2": {"nombre": "Thriller", "Artista": "The Weeknd", "Genero": "R&B", "cantidad": 3},
    "3": {"nombre": "Discovery", "Artista": "Daft Punk", "Genero": "Techno", "cantidad": 2},
    "4": {"nombre": "Bad", "Artista": "Michael Jackson", "Genero": "Pop", "cantidad": 7},
    "5": {"nombre": "Abbey Road", "Artista": "The Beatles", "Genero": "Rock", "cantidad": 1},
    "6": {"nombre": "Abbey Road", "Artista": "Red Hot Chili Peppers", "Genero": "Rock", "cantidad": 4},
    "7": {"nombre": "Bad", "Artista": "U2", "Genero": "Rock", "cantidad": 6},
    "8": {"nombre": "Cómo te voy a olvidar", "Artista": "Los Ángeles Azules", "Genero": "Cumbia", "cantidad": 2},
    "9": {"nombre": "Currents", "Artista": "Tame Impala", "Genero": "Indie", "cantidad": 8},
    "10": {"nombre": "The Four Seasons", "Artista": "Antonio Vivaldi", "Genero": "Clásica", "cantidad": 3},
    "11": {"nombre": "Discovery", "Artista": "Coldplay", "Genero": "Pop", "cantidad": 2}
}

nombrealbum = {
    "thriller": {1, 2},  
    "discovery": {3, 11},  
    "bad": {4, 7},  
    "abbey road": {5, 6},  
    "cómo te voy a olvidar": {8},
    "currents": {9},
    "the four seasons": {10}
}

generos = {
    "pop": {1, 2, 11},
    "r&b": {2},
    "techno": {3},
    "rock": {5, 6, 7},
    "cumbia": {8},
    "indie": {9},
    "clasica": {10}
}

artistas = {
    "michael jackson": {1, 4},
    "the weeknd": {2},
    "daft punk": {3},
    "the beatles": {5},
    "red hot chili peppers": {6},
    "u2": {7},
    "los ángeles azules": {8},
    "tame impala": {9},
    "antonio vivaldi": {10},
    "coldplay": {11}
}"""

"""Usuarios={
    "0001":{"nombre": "Juan", "apellido": "Perez", "dni": "12345678"},
    "0002":{"nombre": "Ana", "apellido": "Gomez", "dni": "23456789"},
    "0003":{"nombre": "Luis", "apellido": "Martinez", "dni": "34567890"},
    "0004":{"nombre": "Maria", "apellido": "Lopez", "dni": "45678901"},
    "0005":{"nombre": "Carlos", "apellido": "Sanchez", "dni": "56789012"}
}"""

#Matrices
"""Prestamos=[
    ["0001", 'Disco 1', "2024-06-16", '2024-06-30', 400, False],
    ["0001", 'Disco 4', '2024-06-13', '2024-07-14', 700, False],
    ["0004", 'Disco 6', '2024-06-14', '2024-08-16', 1000, True],
    ["0005", 'Disco 4', '2024-06-14', '2024-08-16', 1000, True]
]"""
uso=0
while uso==0:
    print()
    print('1 Discos')
    print('2 Usuarios')
    print('3 Prestamos')
    print('4 Devoluciones')
    print('0 Salir')
    try:
        funcion = int(input("Ingrese que funcion quiere realizar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue  # Regresa al inicio del bucle si hay un error de entrada
    if funcion==1:
        loop=0
        while loop==0:
            print('ingrese un numero del 0 al 4')
            print('1: Agregar Discos ➕')
            print('2: Modificar Discos ⚙')
            print('3: Eliminar Discos ✖')
            print('4: Ver Stock 👀')
            print('0: Volver')
            try:
                menu = int(input())
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue  # Regresa al inicio del bucle si hay un error de entrada
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
            else:
                print('Opcion no valida')

    elif funcion == 2:
        Usuarios = Personas.cargar_personas()  
        while True:
            print("\nMenu de Personas:")
            print("1. Agregar persona")
            print("2. Mostrar personas")
            print("3. Modificar persona")
            print("4. Eliminar persona")
            print("0. Volver")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                dni = input("Ingrese el DNI de la persona: ")  
                nombre = input("Ingrese el nombre de la persona: ")
                apellido = input("Ingrese el apellido de la persona: ")  
                Personas.agregar_persona(Usuarios, dni, nombre, apellido)  
            
            elif opcion == '2':
                Personas.mostrar_personas(Usuarios)
            
            elif opcion == '3':
                Personas.mostrar_personas(Usuarios)
                id_persona = input("Ingrese el ID de la persona que desea modificar: ")
                id_persona=f"{id_persona:<4}"
                
                verificacionuserid=validaciones.ValidUserid(id_persona) #Se verifica que el user cargado coincida con el parametro regex.
    
                while verificacionuserid == False:
                    print("Nro de cliente no valido")
                    id_persona=input("Ingrese un numero de cliente valido: ")
                    id_persona=(f"{id_persona:0>4}")
                    verificacionuserid=validaciones.ValidUserid(id_persona)
        
                
                if id_persona in Usuarios:
                    nuevo_dni = input("Ingrese el nuevo DNI (deje en blanco para no modificar): ")
                    nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no modificar): ")
                    nuevo_apellido = input("Ingrese el nuevo apellido (deje en blanco para no modificar): ")

                    # Verificar si se deben modificar los valores
                    Personas.modificar_persona(Usuarios, id_persona, 
                        nuevo_dni if nuevo_dni else None, 
                        nuevo_nombre if nuevo_nombre else None, 
                        nuevo_apellido if nuevo_apellido else None)
                else:
                    print("ID no encontrado. Intente de nuevo.")
            
            elif opcion == '4':
                Personas.mostrar_personas(Usuarios)
                id_persona = input("Ingrese el ID de la persona que desea eliminar: ")
                id_persona=f"{id_persona:<4}"
                
                if id_persona in Usuarios:
                    Personas.eliminar_persona(Usuarios, id_persona)
                else:
                    print("ID no encontrado. Intente de nuevo.")
            
            elif opcion == '0':
                break
            else:
             print("Opción no válida. Intente de nuevo.")
    
    elif funcion==3:
        loop_prestamos=0
        while loop_prestamos== 0 :
            print("\nMenu")
            print('1 Crear prestamos ➕')
            print('2 Modificar prestamos ➖')
            print('3 Eliminar prestamo ⚙️')
            print('4 Mostrar listado 👀')
            print('5 Cantidad de discos disponibles')
            print('6 Busqueda por fecha de vencimiento')
            print("0 volver")
            while True :
                try:
                    menu_prestamos=int(input("Ingrese que función desea realizar:"))
                except ValueError:
                    print("El valor debe ser un número\n")
                    continue
                if menu_prestamos >=7 or menu_prestamos<0:
                    print("El valor ingresado no es correcto\n")
                else :
                    break
            
            match menu_prestamos :
                
                case 1: # Creación 
                    print("\n Creación de prestamo ")
                    Verfificar_información=True 
                    while Verfificar_información==True:
                        Usuarios = Personas.cargar_personas()  
                        Personas.mostrar_personas(Usuarios)
                        
                        print()
                        nrocliente=(input("Ingrese el numero de cliente: "))
                        nrocliente=(f"{nrocliente:0>4}")
                        verificacionuserid=validaciones.ValidUserid(nrocliente) #Se verifica que el user cargado coincida con el parametro regex.
                        while verificacionuserid == False:
                            print("Nro de cliente no valido")
                            nrocliente=input("Ingrese un numero de cliente valido: ")
                            nrocliente=(f"{nrocliente:0>4}")
                            verificacionuserid=validaciones.ValidUserid(nrocliente)
                        
                        user=validaciones.existenciadeuser((f"{nrocliente:0>4}"),"Db/personas.json") #Validacion de existencia del usuario
                        if user == True:
                            print("Cliente encontrado")
                    
                        else:
                            print("El usuario no fue encontrado")  #Si el usuario no esta registrado regresa al menu principal 
                            print("Debe registrar al usuario")
                            Verfificar_información=False
                            break  
                        DiscosStock.mostrar()        
                        print("\nBusqueda de album")
                         
                        #Se llama a la funcion para verificar la disponibilidad del album                       
                        diccionarios_elegidos=funcionesvarias.menu_busqueda_album(r"Db\discos.json")
                        
                        if len(diccionarios_elegidos)>1: #En caso de que se haya encontrado más de una coincidencia
                            while True:
                                try:    
                                    idelegido=int(input("Ingrese id que desea retirar:"))
                                except ValueError:
                                    print("El valor debe ser un numero")
                                    continue
                                if idelegido < 0 :
                                    print("El valor debe ser positivo")
                                    continue
                                else:
                                    break
                        else: 
                            idelegido = list(diccionarios_elegidos.keys())[0] #Almaceno la unica key devulta
                            
                        nombredelalbum=diccionarios_elegidos[str(idelegido)]["nombre"]
                        iddisco=str(idelegido)
                        funcionesvarias.retirar_Disco("Db/discos.json",idelegido)
                        
                        while True:
                            try:
                                diasdeprestamos=int(input("Ingrese cuantos dias se realizara el prestamo: "))
                            except TypeError:
                                print("El valor debe ser un numero entero")
                                continue
                            if diasdeprestamos >60:
                               print ("Excede el numero de dias de prestamo")

                            else: 
                                break
                        
                        
                        monto=int(input("Ingrese el monto total del prestamo: "))
                        prestamos.crear_prestamos(nrocliente, nombredelalbum,iddisco,diasdeprestamos,monto ,r"Db\prestamos_db.txt")
                        Verfificar_información=False        
                        
                case 2 :# Modicación 
                        print("Modificación de prestamos \n")
                        userid=(input("Ingrese el id del usuario del registro a modificar: "))
                        userid=(f"{userid:0>4}")
                    
                        verificacionuserid=validaciones.ValidUserid(userid) #Se verifica que el user cargado coincida con el parametro regex.
                        while verificacionuserid == False:
                            print("Nro de cliente no valido")
                            userid=input("Ingrese un numero de cliente valido: ")
                            userid=(f"{userid:0>4}")
                            verificacionuserid=validaciones.ValidUserid(userid)
                        
                        user=validaciones.existenciadeuser((f"{userid:0>4}"),"Db/personas.json") #Validacion de existencia del usuario
                        if user == True:
                            print("Cliente encontrado")
                    
                        else:
                            print("El usuario no fue encontrado")  #Si el usuario no esta registrado regresa al menu principal 
                            print("Debe registrar al usuario")
                            Verfificar_información=False
                            break  
                                
                        existencia=validaciones.existenciadeuser(userid,"Db/personas.json")
                            
                        prestamos.modificar_prestamos(userid,"Db/personaDb/prestamos_db.txt","Db/discos.json")
                case 3 :# Eliminación
                    print("\n Eliminación de prestamos")
                    userid=(input("Ingrese el id del usuario del registro a modificar: "))
                    userid=(f"{userid:0>4}")
                    verificacionuserid=validaciones.ValidUserid(userid) #Se verifica que el user cargado coincida con el parametro regex.
                    while verificacionuserid == False:
                        print("Nro de cliente no valido")
                        userid=input("Ingrese un numero de cliente valido: ")
                        userid=(f"{userid:0>4}")
                        verificacionuserid=validaciones.ValidUserid(userid)
                    
                    user=validaciones.existenciadeuser(userid,"Db/personas.json") #Validacion de existencia del usuario
                    if user == True:
                        print("Cliente encontrado")
                
                    else:
                        print("El usuario no fue encontrado")  #Si el usuario no esta registrado regresa al menu principal 
                        print("Debe registrar al usuario")
                        Verfificar_información=False
                        break  
                    
                    prestamos.eliminar_prestamos(userid,"Db/prestamos_db.txt")
                case 4 :# Mostrar
                    prestamos.mostrar_prestamos("Db/prestamos_db.txt")
                
                case 5: #Sumatoria de cantidad de discos disponibles
                    discos=DiscosStock.cargar_disco()
                    funcionesvarias.json_a_ndjson(discos)
                    total=funcionesvarias.suma_cantidad_discos("Db/discos.ndjson")
                    if total:
                        print(f"\n El total de discos disponibles es de {total}")
                    else:
                        print("No se pudo realizar la sumatoria")
                
                case 6: 
                    print("Tenga en cuenta el formato:xxxx-xx-xx (año-mes-dia)\n")
                    fechadebusqueda=input("Ingrese la fecha por la cual quiere realizar el filtro: ")
                    caso1=validaciones.validaciondefecha(fechadebusqueda)
                    while caso1== False:
                        print("El formato de fecha no es el correcto")
                        print("xxxx-xx-xx")   
                        fechadebusqueda=input()
                        caso1=validaciones.validaciondefecha(fechadebusqueda)
                        
                    prestamos.prestamos_vencidos(fechadebusqueda,"Db/prestamos_db.txt")
                    
                    
                   
            if menu_prestamos == 0:
                loop_prestamos=1
    
    elif funcion==4:
        loop_devoluciones=0
        while loop_devoluciones==0:
            print('1 Devolver un disco ➕')
            print("0 volver")
            menu_devoluciones = int(input('Ingrese una acción:' ))
            
            if menu_devoluciones==1:
            
                print("\n Devolución de discos ")
                
                control=False
                while control==False:
                    userid=input("Ingrese el id del usuario: ")
                    userid=f"{userid:<4}"
                    verificacionuserid=validaciones.ValidUserid(userid) #Se verifica que el user cargado coincida con el parametro regex.
                    while verificacionuserid == False:
                        print("Nro de cliente no valido")
                        userid=input("Ingrese un numero de cliente valido: ")
                        userid=f"{userid:<4}"
                        verificacionuserid=validaciones.ValidUserid(userid)
                    
                    aparaiciones=prestamos.busqueda_prestamos(userid,r"Db/prestamos_db.txt","False")
                    if aparaiciones==False:
                        print("El prestamo no fue encontrado \n")  
                    else:
                        n_aparicion=input("Qué prestamo desea culminar? ")
                        aparaiciones[n_aparicion][-1]='True'
                        posicion=aparaiciones[n_aparicion][2]
                        prestamo_actualizado=",".join(aparaiciones[n_aparicion])
                        prestamos.actualizar_txt(r"Db/prestamos_db.txt",prestamo_actualizado,n_aparicion,True)
                        disco=DiscosStock.cargar_disco()
                        disco[str(posicion)]['cantidad']+=1
                        DiscosStock.guardar_disco(disco)
                    control=True
    
            elif menu_devoluciones==0:
                loop_devoluciones=1
        
    elif funcion ==0 :
        uso=1
    else:
        print('Numero no valido')

