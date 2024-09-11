import re 
import validaciones
#validaciones

#validar que el dni no se reptia
def dnirep(dni):
    for persona in customer:
        if persona["dni"] == dni:
            return True  
    return False  

#fin validaciones


# Lista de los clientes
customer = []


# Función para agregar clientes
def addcustomer():
    nombreapellido = input("Ingrese el nombre y apellido: ")
    dni = input("Ingrese el DNI sin puntos ni espacios: ")

    # Validaciónes del DNI
    if not validaciones.ValidDNI(dni):
        print("DNI inválido. Debe contener entre 7 y 8 dígitos sin puntos ni espacios.")
        return
    #validaciones del nombre y apellido
    if not validaciones.ValidUsername(nombreapellido):
        print("El nombre o apellido contiene caracteres inválidos.")
        return

    newcustomer = {"nombre y apellido": nombreapellido, "dni": dni}
    customer.append(newcustomer)
    print(f"Cliente {nombreapellido} agregado exitosamente.")
    
def modcustomer():
    dni = input("Ingrese el DNI de la persona a modificar: ")
    
    # Búsqueda del cliente con el DNI
    for persona in customer:
        if persona["dni"] == dni:
            nuevo_nya = input("Ingrese el nuevo nombre: ")

            if not validaciones.ValidUsername(nuevo_nya):
                print("El nuevo nombre o apellido contiene caracteres inválidos.")
                return
            persona["nombre y apellido"] = nuevo_nya
            print("Datos actualizados.")
            return
    print("Persona no encontrada.")

def delcustomer():
    dni = input("Ingrese el DNI de la persona a eliminar: ")

    # Eliminamos la persona con el DNI
    for persona in customer:
        if persona["dni"] == dni:
            customer.remove(persona)
            print("Persona eliminada.")
            return
    print("Persona no encontrada.")

def listcustomer():
    if not customer:
        print("No hay personas registradas.")
    else:
        for persona in customer:
            print(f"Nombre y apellido: {persona['nombreapellido']} - DNI: {persona['dni']}")

