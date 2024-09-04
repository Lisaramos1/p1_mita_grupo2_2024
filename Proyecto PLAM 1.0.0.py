import DiscosStock 
import prestamos 
discos=[]
uso=0
while uso==0:
    print('1 Discos')
    print('2 Usuarios')
    print('3 Prestamos')
    print('4 Salir')
    funcion = int(input('ingrese un numero del 1 al 4 segun que necesite: '))
    if funcion==1:
        DiscosStock.crud_discos()
    elif funcion==2:
        fusuarios
    elif funcion==3:
        prestamos.crud_prestamos()
    else:
        uso=0

