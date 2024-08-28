import DiscosStock
discos=[]
uso=0
while uso==0:
    print('Discos')
    print('Usuarios')
    print('Prestamos')
    print('Salir')
    funcion = int(input('ingrese un numero del 1 al 4 segun que necesite: '))
    if funcion==1:
        DiscosStock()
    elif funcion==2:
        fusuarios()
    elif funcion==3:
        fprestamos()
    else:
        uso=0
