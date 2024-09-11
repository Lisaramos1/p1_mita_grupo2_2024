        menu = int(input('Ingrese una acción: '))
        if menu == 1:
            crear_prestamos()
        elif menu == 2:
            modificar_prestamos() 
        elif menu == 3:
            eliminar_prestamos()
        elif menu == 4:
            mostrar_prestamos() 
        elif menu == 0:
            loop = 1
        else: 
            print("Ingrese un número válido")
