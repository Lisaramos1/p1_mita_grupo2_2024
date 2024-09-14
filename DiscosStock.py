discos = {
    {'id':1,'nombre':'Disco 1','Artista':A,'Genero':Rock,'cantidad':5},
    {'id':2,'nombre':'Disco 2','cantidad':3},
    {'id':3,'nombre':'Disco 3','cantidad':2},
    {'id':4,'nombre':'Disco 4','cantidad':7},
    {'id':5,'nombre':'Disco 5','cantidad':1},
    {'id':6,'nombre':'Disco 6','cantidad':4},
    {'id':7,'nombre':'Disco 7','cantidad':6},
    {'id':8,'nombre':'Disco 8','cantidad':2},
    {'id':9,'nombre':'Disco 9','cantidad':8},
    {'id':10,'nombre':'Disco 10','cantidad':3}
}

def menu():
    print('ingrese un numero del 0 al 4')
    print('1: Agregar Discos ➕')
    print('2: Modificar Discos ⚙')
    print('3: Eliminar Discos ✖')
    print('4: Ver Stock 👀')
    print('0: Volver')

def limpiar(): #posible funcion futura para que limpie la terminal
    print()

def agregar(): #agregar discos 
    print('Ingrese el nombre del disco, ingrese 0 para volver')
    nombre = input()
    if nombre =='0': #verifica la exepcion 
        print()
        return
    for i, (numero , nombred ,cantidad) in enumerate(discos): #busca el disco solicitado
        if nombre == nombred:
            discos[i] = (numero, nombred,cantidad + 1)  # Modifica la tupla en su lugar
            print(discos)
            print()
            return        
    discos.append((len(discos)+1,nombre,1)) #crea un disco completamente nuevo
    print(discos)
    print()
    return

def modificar(): #funcion que modifica un disco
    print('Ingrese el numero del disco que desee modificar, ingrese 0 para volver')
    print(discos)
    nro = int(input())
    if nro==0: #verifica la excepcion
        print()
        return
    for i, (numero , nombre ,cantidad) in enumerate(discos): #busca en la tabla discos un disco especifico
        if numero == nro :
            print(f'el disco que sera modificado es {discos[i]}') #informa que disco sera modificado
            print('Ingrese el nuevo nombre del disco, si no es el disco que desea modificar, ingrese 0')
            nuevo = input()
            if nuevo == '0': #verifica la excepcion
                print()
                return
            if nuevo ==nombre: #si el nuevo nombre esta repetido se suma a la cantidad de esos discos
                discos[i] = (numero, nuevo, cantidad+1)
                print()
                return    
            discos[i] = (numero, nuevo, 1) #si es completamente nuevo se le asignan los valores
            print()
            return
    print(f'\033[31mDisco no encontrado\033[0m') #color rojo
    print()
    return

def eliminar():#funcion que elimina un dato de la tabla discos
    print('Ingrese el numero del disco que desee eliminar, ingrese 0 para volver')
    print(discos)
    nro = int(input())
    if nro==0: #verifica la excepcion
        print()
        return
    for i, (numero , nombre , cantidad) in enumerate(discos): #busca el disco solicitado
        if numero == nro :
            print(f'el disco que sera eliminado es {discos[i]}') #pregunta si el disco es correcto
            print('Ingrese 1 para confirmar si no ingrese 0')
            nuevo = input()
            if nuevo == '0': #verifica la excepcion
                print()  
                return
            discos.pop(i)    
            print(discos)
            print()
            return
    print(f'\033[31mDisco no encontrado\033[0m') #color rojo
    return

def mostrar():
    for i in discos: #printea la lista de discos
        print(i)
    print()
    return