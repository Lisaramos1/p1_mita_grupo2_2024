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
        prestamos.crud_prestamos()
        
    else:
        uso=1
