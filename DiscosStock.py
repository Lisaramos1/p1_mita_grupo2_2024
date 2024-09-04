
def agregar():
    print('Ingrese el nombre del disco, ingrese -1 para volver')
    nombre = input()
    discos.append(nombre)


def menudiscos():
    menu=0
    while menu==0:
        print('1 Agregar discos')
        print('2 Modificar discos')
        print('3 Eliminar discos')
        print('4 Rentar discos')
        print('0 Volver')
        menu = int(input('que desearia hacer: '))
        if menu==1:
            agregar
        elif menu==2:
            modificar
        elif menu==3:
            eliminar
        elif menu==4:
            rentar
        elif menu==0:
            return
