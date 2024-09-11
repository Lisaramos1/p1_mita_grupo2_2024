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
        DiscosStock.menudiscos()
        
    elif funcion==2:
        Personas.menue()
    if funcion==3:
        prestamos.crud_prestamos()
    else:
        uso=1
