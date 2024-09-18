def agregar(discos):
    print('Ingrese el nombre del disco, ingrese 0 para volver')
    nombre = input()
    if nombre == '0':
        return discos
    
    # Verificar si el disco ya existe para actualizar la cantidad
    for disco in discos:
        if nombre == disco['nombre']:
            disco['cantidad'] += 1
            print(f"Disco actualizado: {disco}")
            return discos

    # Si el disco no existe, solicitar más datos
    print('Ingrese el artista del disco:')
    artista = input()
    
    print('Ingrese el género del disco:')
    genero = input()

    nuevo_id = len(discos) + 1

    nuevo_disco = { # Crea el disco nuevo y lo agrega 
        'id': nuevo_id,
        'nombre': nombre,
        'Artista': artista,
        'Genero': genero,
        'cantidad': 1
    }
    
    discos.append(nuevo_disco)
    print(f"Disco agregado: {nuevo_disco}")
    
    return discos #Actualiza los discos del main


def modificar(discos):
    mostrar(discos)
    print('Ingrese el número del disco que desee modificar, ingrese 0 para volver')
    nro = int(input())
    if nro == 0:
        return discos

    for disco in discos:
        if disco['id'] == nro:
            print(f'El disco que será modificado es {disco}')
            print('Ingrese el nuevo nombre del disco, o presione Enter para no modificar:')
            nuevo_nombre = input()
            if nuevo_nombre:
                disco['nombre'] = nuevo_nombre
            if nuevo_nombre:
                for d in discos:
                    if d['nombre'] == nuevo_nombre:
                        # Si el nombre ya existe, incrementamos la cantidad del disco existente
                        d['cantidad'] += disco['cantidad']
                        print(f"El disco {d['nombre']} ya existe, se ha incrementado la cantidad a {d['cantidad']}")
                        discos.remove(disco)  # Eliminamos el disco que iba a ser modificado
                        return discos
                disco['nombre'] = nuevo_nombre  # Si no existe, modificamos el nombre    

            print('Ingrese el nuevo artista del disco, o presione Enter para no modificar:')
            nuevo_artista = input()
            if nuevo_artista:
                disco['Artista'] = nuevo_artista

            print('Ingrese el nuevo género del disco, o presione Enter para no modificar:')
            nuevo_genero = input()
            if nuevo_genero:
                disco['Genero'] = nuevo_genero

            print(f"Disco modificado: {disco}")
            return discos
    
    print(f'\033[31mDisco no encontrado\033[0m')
    return discos


def eliminar(discos):
    mostrar(discos)
    print('Ingrese el número del disco que desee eliminar, ingrese 0 para volver')
    nro = int(input())
    if nro == 0:
        return discos
    
    for i, disco in enumerate(discos):
        if disco['id'] == nro:
            print(f'El disco que será eliminado es {disco}')
            print('Ingrese 1 para confirmar, o ingrese 0 para cancelar')
            confirmacion = input()
            if confirmacion == '1':
                discos.pop(i)
                print(f"Disco {nro} eliminado.")
                return discos
            else:
                print("Eliminación cancelada.")
                return discos

    print(f'\033[31mDisco no encontrado\033[0m')
    return discos


def mostrar(discos):
    if not discos:
        print("No hay discos en la lista.")
        return

    for disco in discos:
        print(f"ID: {disco['id']}, Nombre: {disco['nombre']}, Artista: {disco['Artista']}, Género: {disco['Genero']}, Cantidad: {disco['cantidad']}")
    print()