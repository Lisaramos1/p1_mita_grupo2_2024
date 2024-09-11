import DiscosStock
import prestamos
import Usuarios

uso=0
while uso==0:
    print('1 Discos')
    print('2 Usuarios')
    print('3 Prestamos')
    print('0 Salir')
    funcion = int(input())
    if funcion==1:
        DiscosStock.menudiscos()   
    elif funcion==2:
        Usuarios()
    if funcion==3:
        prestamos.crud_prestamos()
    else:
        uso=1

def Usuarios(): 
    while True:
        print('1 Agregar Usuario')
        print('2 Modificar Usuario')
        print('3 Eliminar Usuario')
        print('4 Mostrar la lista de Usuarios')
        print('0 Volver')
        menu = input('¿Qué desea hacer?: ')

        if menu == '1':
            addcustomer()
        elif menu == '2':
            modcustomer()
        elif menu == '3':
            delcustomer()
        elif menu == '4':
            listcustomer()
        elif menu == '0':
            print("Volviendo al menú principal.")
            return
        else:
            print("Opción no válida.")
        menu = 0