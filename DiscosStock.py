import json

# Función para cargar el archivo JSON como un diccionario en Python
def cargar_disco():
    try:
        with open("Db/discos.json", "r", encoding="utf-8") as archivo:
            discos = json.load(archivo)
    except FileNotFoundError:
        print("Archivo JSON no encontrado.")
    return discos

# Función para guardar el diccionario en el archivo JSON
def guardar_disco(discos):
    with open("Db/discos.json", "w", encoding="utf-8") as archivo:
        json.dump(discos, archivo, indent=4)


# Función para agregar un disco al inventario
def agregar():
    discos = cargar_disco()  # Cargar los datos del archivo JSON

    nombre = input("Ingrese el nombre del disco: ").strip().capitalize()
    artista = input("Ingrese el nombre del artista: ").strip().capitalize()
    genero = input("Ingrese el género del disco: ").strip().capitalize()

    try:
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Cantidad no válida. Debe ser un número entero.")
        return

    # Buscar si el disco ya existe con el mismo nombre y artista
    disco_existente = None
    for key, disco in discos.items():
        if disco['nombre'].lower() == nombre.lower() and disco['Artista'].lower() == artista.lower():
            disco_existente = key
            break

    # Si existe, sumamos la cantidad
    if disco_existente:
        discos[disco_existente]['cantidad'] += cantidad
        print(f"Disco existente. Actualizada cantidad a {discos[disco_existente]['cantidad']}.")
    else:
        # Encontrar el primer ID disponible
        ids_existentes = {int(k) for k in discos.keys()}  # Convertir las claves a enteros
        nuevo_id = 1
        while nuevo_id in ids_existentes:
            nuevo_id += 1  # Buscar el primer número que no esté en los IDs existentes

        discos[str(nuevo_id)] = {
            "nombre": nombre,
            "Artista": artista,
            "Genero": genero,
            "cantidad": cantidad
        }
        print(f"Disco '{nombre}' agregado exitosamente con ID {nuevo_id}.")
    guardar_disco(discos)  # Guardar el cambio en el archivo

# Función para modificar los datos de un disco existente
def modificar():
    discos = cargar_disco()  # Cargar los datos del archivo JSON

    mostrar(discos)
    id_disco = input("Ingrese el ID del disco que desea modificar: ").strip()

    if id_disco not in discos:
        print("ID no encontrado.")
        return

    # Modificación de los atributos
    nombre = input(f"Nombre actual ({discos[id_disco]['nombre']}): ").strip() or discos[id_disco]['nombre']
    artista = input(f"Artista actual ({discos[id_disco]['Artista']}): ").strip() or discos[id_disco]['Artista']
    genero = input(f"Género actual ({discos[id_disco]['Genero']}): ").strip() or discos[id_disco]['Genero']
    
    try:
        cantidad = int(input(f"Cantidad actual ({discos[id_disco]['cantidad']}): ").strip() or discos[id_disco]['cantidad'])
    except ValueError:
        print("Cantidad no válida. No se aplicaron cambios a la cantidad.")
        return

    # Actualización
    discos[id_disco].update({
        "nombre": nombre,
        "Artista": artista,
        "Genero": genero,
        "cantidad": cantidad
    })
    print("Disco modificado exitosamente.")

    guardar_disco(discos)  # Guardar el cambio en el archivo

# Función para eliminar un disco del inventario
def eliminar():
    discos = cargar_disco()  # Cargar los datos del archivo JSON
    mostrar(discos)
    id_disco = input("Ingrese el ID del disco que desea eliminar: ").strip()

    if id_disco in discos:
        del discos[id_disco]
        print(f"Disco con ID {id_disco} eliminado exitosamente.")
        guardar_disco(discos)
    else:
        print("ID no encontrado.")

# Función para mostrar los discos disponibles
def mostrar(discos=None):
    if discos is None:  # Cargar los datos solo si no se pasan como argumento
        discos = cargar_disco()
    for id_disco, info in discos.items():
        print(f"ID: {id_disco}, Nombre: {info['nombre']}, Artista: {info['Artista']}, Género: {info['Genero']}, Cantidad: {info['cantidad']}")