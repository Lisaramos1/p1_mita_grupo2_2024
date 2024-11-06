import json
from funcionesvarias import generadorid  
from validaciones import Valdni, ValidUsername

route = "Db/personas.json"
backup_route = "Db/personas_backup.json"

def cargar_personas():
    try:
        with open(route, 'r') as file:
            Usuarios = json.load(file)
        return Usuarios  
    except FileNotFoundError:
        with open(route, 'w') as file:
            json.dump({}, file)  
        print(f'El archivo {route} no se encontró. Se ha creado uno nuevo.')
        return {}  
    except PermissionError:
        print(f'Error de permisos al intentar abrir {route}.')
        return {}
    except json.JSONDecodeError:
        print(f'Error al decodificar el JSON en {route}.')
        return {}

def guardar_personas(Usuarios):
    with open(route, 'w') as file:
        json.dump(Usuarios, file, indent=4)  

def backup_personas(Usuarios):
    with open(backup_route, 'w') as backup_file:
        json.dump(Usuarios, backup_file, indent=4)
    print(f"Backup realizado en {backup_route}")

def agregar_persona(Usuarios, dni, nombre, apellido):
    # Validar el DNI
    if not Valdni(dni, Usuarios):
        return
    
    # Validar el nombre y apellido
    if not ValidUsername(nombre):
        print("El nombre contiene caracteres inválidos.")
        return  

    if not ValidUsername(apellido):
        print("El apellido contiene caracteres inválidos.")
        return 

    
    nuevo_id = generadorid(Usuarios)  
    Usuarios[nuevo_id] = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni
    }

    guardar_personas(Usuarios) 
    backup_personas(Usuarios)  
    print(f"Persona agregada exitosamente: {nombre} {apellido} (DNI: {dni}, ID: {nuevo_id})")

def mostrar_personas(Usuarios):
    if not Usuarios:
        print("No hay personas registradas.")
    else:
        for id_persona, datos in Usuarios.items():
            print(f"ID: {id_persona}, DNI: {datos['dni']}, Nombre: {datos['nombre']}, Apellido: {datos['apellido']}")

def modificar_persona(Usuarios, id_persona, nuevo_dni=None, nuevo_nombre=None, nuevo_apellido=None):
    if id_persona in Usuarios:
        if nuevo_dni:
            Usuarios[id_persona]['dni'] = nuevo_dni
        if nuevo_nombre:
            Usuarios[id_persona]['nombre'] = nuevo_nombre
        if nuevo_apellido:
            Usuarios[id_persona]['apellido'] = nuevo_apellido
        print(f"Persona modificada: {Usuarios[id_persona]}")
        guardar_personas(Usuarios)  # Guarda el diccionario actualizado
        backup_personas(Usuarios) # Guarda actualizado en el backup
    else:
        print("ID no válido.")

def eliminar_persona(Usuarios, id_persona):
    if id_persona in Usuarios:
        removed_person = Usuarios.pop(id_persona)
        print(f"Persona eliminada: {removed_person}")
        guardar_personas(Usuarios)  # Guarda el diccionario actualizado
    else:
        print("ID no válido.")

# función para hacer backup de los datos
def backup_personas(Usuarios):
    backup_route = "Db/personas_backup.json"
    with open(backup_route, 'w') as backup_file:
        json.dump(Usuarios, backup_file, indent=4)
    print(f"Backup realizado en {backup_route}")
