import DiscosStock
discos=[]
uso=0
while uso==0:
    print('1 Discos')
    print('2 Usuarios')
    print('3 Prestamos')
    print('4 Salir')
    funcion = int(input('ingrese un numero del 1 al 4 segun que necesite: '))
    if funcion==1:
        fdiscos()
    elif funcion==2:
        fusuarios()
    elif funcion==3:
        fprestamos()
    else:
        uso=0
