import DiscosStock
uso=0
while uso==0:
    print('1 Discos')
    print('2 Usuarios')
    print('3 Prestamos')
    print('0 Salir')
    funcion = int(input())
    if funcion==1:
        DiscosStock.menudisco()
    if funcion==2:
        fusuarios()
    if funcion==3:
        fprestamos()
    if funcion==0:
        uso=1