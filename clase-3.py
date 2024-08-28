discos=[]
uso=0
def fdiscos():
    print('Agregar discos')
    print('Modificar discos')
    print('Eliminar discos')
    print('Rentar discos')
    print('Volver')
    print()
    funcion = int(input('que desearia hacer:'))






while uso==0:
    print('Discos')
    print('Usuarios')
    print('Prestamos')
    print('Salir')
    funcion = int(input('ingrese un numero del 1 al 4 segun que necesite: '))
    if funcion==1:
        fdiscos()
    elif funcion==2:
        fusuarios()
    elif funcion==3:
        fprestamos()
    else:
        uso=0
