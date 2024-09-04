discos = []

def limpiar():
    print()

def agregar():
    print('Ingrese el nombre del disco, ingrese 0 para volver')
    nombre = input()
    if nombre =='0':
        print()
        return
    for i, (numero , nombred , estado , cantidad) in enumerate(discos):
        if nombre == nombred:
            discos.append((len(discos)+1,nombre,'disponible',cantidad+1))
            print(discos)
            print()
            return        
    discos.append((len(discos)+1,nombre,'disponible',1))
    print()
    return

def modificar():
    print('Ingrese el numero del disco que desee modificar, ingrese 0 para volver')
    print(discos)
    nro = int(input())
    if nro==0:
        print()
        return
    for i, (numero , nombre , estado , cantidad) in enumerate(discos):
        if numero == nro :
            print(f'el disco que sera modificado es {discos[i]}')
            print('Ingrese el nuevo nombre del disco, si no es el disco que desea modificar, ingrese 0')
            nuevo = input()
            if nuevo == '0':
                print()
                return
            if nuevo ==nombre:
                discos[i] = (numero, nuevo, estado, cantidad+1)
                print()
                return    
            discos[i] = (numero, nuevo, estado, 1)
            print()
            return
    
    print(f'\033[31mDisco no encontrado\033[0m')
    print()
    return

def eliminar():
    print('Ingrese el numero del disco que desee eliminar, ingrese 0 para volver')
    print(discos)
    nro = int(input())
    if nro==0:
        print()
        return
    for i, (numero , nombre , estado , cantidad) in enumerate(discos):
        if numero == nro :
            print(f'el disco que sera eliminado es {discos[i]}')
            print('Ingrese 1 para confirmar si no ingrese 0')
            nuevo = input()
            if nuevo == '0':
                print()  
                return
            discos.pop(i)    
            print(discos)
            print()
            return
    print(f'\033[31mDisco no encontrado\033[0m')
    return

def mostrar():
    for i in discos:
        print(i)
    print()
    return

def menudiscos():
    loop=0
    while loop==0:
        print('1 Agregar discos ➕')
        print('2 Modificar discos ⚙')
        print('3 Eliminar discos ❌')
        print('4 Visualizar discos 👀')
        print('0 Volver ')
        menu = int(input('que desearia hacer: '))
        if menu==1:
            agregar()
        elif menu==2:
            modificar()
        elif menu==3:
            eliminar()
        elif menu==4:
            mostrar()
        elif menu==0:
            loop=1
            return
        else:  
            print('Ingrese un numero valido')
