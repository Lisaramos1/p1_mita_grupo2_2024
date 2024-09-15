import re 
import validaciones
from funcionesvarias import generadorid

# Lista de los clientes
customer = []

# Función para agregar clientes
def addcustomer(nombreapellido, dni):
    # Validación del DNI
    if not validaciones.ValidDNI(dni):
        print("DNI inválido. Debe contener entre 7 y 8 dígitos sin puntos ni espacios.")
        return

    # Validación del nombre y apellido
    if not validaciones.ValidUsername(nombreapellido):
        print("El nombre o apellido contiene caracteres inválidos.")
        return

    id = generadorid(customer)
    
    newcustomer = {"id": id, "nombre y apellido": nombreapellido, "dni": dni}
    customer.append(newcustomer)
    print(f"Cliente {nombreapellido} agregado exitosamente con ID {id}.")
    
# Función para modificar clientes
def modcustomer(dni, nuevo_nya):
    # Búsqueda del cliente con el DNI
    for persona in customer:
        if persona["dni"] == dni:
            if not validaciones.ValidUsername(nuevo_nya):
                print("El nuevo nombre o apellido contiene caracteres inválidos.")
                return
            persona["nombre y apellido"] = nuevo_nya
            print("Datos actualizados.")
            return
    print("Persona no encontrada.")

# Función para eliminar clientes
def delcustomer(dni):
    # Eliminamos la persona con el DNI
    for persona in customer:
        if persona["dni"] == dni:
            customer.remove(persona)
            print("Persona eliminada.")
            return
    print("Persona no encontrada.")

# Función para listar clientes
def listcustomer():
    if not customer:
        print("No hay personas registradas.")
    else:
        for persona in customer:
            print(f"ID: {persona['id']} - Nombre y apellido: {persona['nombre y apellido']} - DNI: {persona['dni']}")

