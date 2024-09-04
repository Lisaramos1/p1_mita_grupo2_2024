import os, subprocess
discos = []

def limpiar():
    print()

def agregar():
    print('Ingrese el nombre del disco, ingrese 0 para volver')
    nombre = input()
    if nombre =='0':
        limpiar()
        return
    discos.append((len(discos)+1,nombre,'disponible'))
    limpiar()
    print(discos)
    return

def modificar():
    print('Ingrese el numero del disco que desee modificar, ingrese 0 para volver')
    print(discos)
    nro = int(input())
    if nro==0:
        limpiar()
        return
    for i, (numero , nombre , estado) in enumerate(discos):
        if numero == nro :
            print(f'el disco que sera modificado es {discos[i]}')
            print('Ingrese el nuevo nombre del disco, si no es el disco que desea modificar, ingrese 0')
            nuevo = input()
            if nuevo == '0':
                limpiar()
                return
            limpiar()
            discos[i] = (numero, nuevo, estado)
            return
    limpiar()
    print('Disco no encontrado')
    return




def menudiscos():
    loop=0
    while loop==0:
        print('1 Agregar discos')
        print('2 Modificar discos')
        print('3 Eliminar discos')
        print('4 Rentar discos')
        print('0 Volver')
        menu = int(input('que desearia hacer: '))
        if menu==1:
            agregar()
        elif menu==2:
            modificar()
        elif menu==3:
            eliminar
        elif menu==4:
            rentar
        else:
            loop=1
            return
