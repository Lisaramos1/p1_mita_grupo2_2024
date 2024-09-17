discos = [
    {'id':1,'nombre':'Disco 1','Artista':'A','Genero':'Rock','cantidad':5},
    {'id':2,'nombre':'Disco 2','Artista':'B','Genero':'Pop','cantidad':3},
    {'id':3,'nombre':'Disco 3','Artista':'C','Genero':'Techno','cantidad':2},
    {'id':4,'nombre':'Disco 4','Artista':'D','Genero':'Dubstep','cantidad':7},
    {'id':5,'nombre':'Disco 5','Artista':'E','Genero':'Rock nacional','cantidad':1},
    {'id':6,'nombre':'Disco 6','Artista':'F','Genero':'Rock cristiano alternativo','cantidad':4},
    {'id':7,'nombre':'Disco 7','Artista':'G','Genero':'Trap','cantidad':6},
    {'id':8,'nombre':'Disco 8','Artista':'H','Genero':'Cumbia','cantidad':2},
    {'id':9,'nombre':'Disco 9','Artista':'I','Genero':'Indie','cantidad':8},
    {'id':10,'nombre':'Disco 10','Artista':'J','Genero':'Clasica','cantidad':3}
]

def menu():
    print('Ingrese un número del 0 al 4')
    print('1: Agregar Discos ➕')
    print('2: Modificar Discos ⚙')
    print('3: Eliminar Discos ✖')
    print('4: Ver Stock 👀')
    print('0: Volver')

def limpiar():  # posible función futura para que limpie la terminal
    print()

def agregar():  # agregar discos 
    print('Ingrese el nombre del disco, ingrese 0 para volver')
    nombre = input()
    if nombre == '0':  # verifica la excepción
        print()
        return
    
    # Verificar si el disco ya existe para actualizar la cantidad
    for disco in discos:
        if nombre == disco['nombre']:
            disco['cantidad'] += 1  # Incrementar la cantidad del disco existente
            print(f"Disco actualizado: {disco}")
            print()
            return

    # Si el disco no existe, solicitar el artista y género
    print('Ingrese el artista del disco:')
    artista = input()
    
    print('Ingrese el género del disco:')
    genero = input()

    nuevo_id = len(discos) + 1
    
    # Crear un nuevo disco
    nuevo_disco = {
        'id': nuevo_id,
        'nombre': nombre,
        'Artista': artista,
        'Genero': genero,
        'cantidad': 1
    }
    
    discos.append(nuevo_disco)
    print(f"Disco agregado: {nuevo_disco}")
    print()


def modificar():  # función que modifica un disco
    mostrar()
    print('Ingrese el número del disco que desee modificar, ingrese 0 para volver')
    nro = int(input())
    if nro == 0:
        return

    for disco in discos:
        if disco['id'] == nro:
            print(f'El disco que será modificado es {disco}')
            
            # Modificar el nombre
            print('Ingrese el nuevo nombre del disco, o presione Enter para no modificar:')
            nuevo_nombre = input()
            if nuevo_nombre:
                disco['nombre'] = nuevo_nombre

            # Modificar el artista
            print('Ingrese el nuevo artista del disco, o presione Enter para no modificar:')
            nuevo_artista = input()
            if nuevo_artista:
                disco['Artista'] = nuevo_artista

            # Modificar el género
            print('Ingrese el nuevo género del disco, o presione Enter para no modificar:')
            nuevo_genero = input()
            if nuevo_genero:
                disco['Genero'] = nuevo_genero

            print(f"Disco modificado: {disco}")
            return
    
    print(f'\033[31mDisco no encontrado\033[0m')


def eliminar():  # función que elimina un dato de la tabla discos
    mostrar()
    print('Ingrese el número del disco que desee eliminar, ingrese 0 para volver')
    nro = int(input())
    if nro == 0:
        return
    
    for i, disco in enumerate(discos):
        if disco['id'] == nro:
            print(f'El disco que será eliminado es {disco}')
            print('Ingrese 1 para confirmar, o ingrese 0 para cancelar')
            confirmacion = input()
            if confirmacion == '1':
                discos.pop(i)
                print(f"Disco {nro} eliminado.")
                return
            else:
                print("Eliminación cancelada.")
                return
    
    print(f'\033[31mDisco no encontrado\033[0m')


def mostrar():
    if not discos:
        print("No hay discos en la lista.")
        return

    for disco in discos:
        print(f"ID: {disco['id']}, Nombre: {disco['nombre']}, Artista: {disco['Artista']}, Género: {disco['Genero']}, Cantidad: {disco['cantidad']}")
    print()
