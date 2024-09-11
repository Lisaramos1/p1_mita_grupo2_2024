customer = []

def addcustomer():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = input("Ingrese el DNI sin puntos ni espacios: ")
    newcustomer = [nombre, apellido, dni]
    customer.append(newcustomer)
    print(f"Cliente {nombre} {apellido} agregado exitosamente")
    return
    """funcion para agregar persons"""


def modcustomer():
    dni = input("Ingrese el DNI de la persona a modificar: ")
    for persona in customer:
        if persona["dni"] == dni:
            nuevonombre = input("Ingrese el nuevo nombre: ")
            nuevoapellido = input("Ingrese el nuevo apellido: ")
            persona["nombre"] = nuevonombre
            persona["apellido"] = nuevoapellido
            print("Datos actualizados.")
            return
    print("Persona no encontrada.")

    """funcion para modificar personas"""


def delcustomer():
    dni = input("Ingrese el DNI de la persona a eliminar: ")
    for persona in customer:
        if persona["dni"] == dni:
            customer.remove(persona)
            print("Persona eliminada.")
            return
    print("Persona no encontrada.")

    """funcion para eliminar personas"""


def listcustomer():
    if len(customer) == 0:
        print("No hay personas registradas.")
    else:
        for persona in customer:
            print(f"Nombre: {persona} - Apellido: {apellido} - DNI: {dni}")
    return
    """funcion para ver la lista de personas"""


def menue():
    menu = 0
    while menu == 0:
        print('1 Agregar persona')
        print('2 Modificar persona')
        print('3 Eliminar persona')
        print('4 mostrar la lista de personas')
        print('0 Volver')
        menu = int(input('¿Qué desea hacer?: '))
        if menu == 1:
            addcustomer()
        elif menu == 2:
            modcustomer()
        elif menu == 3:
            delcustomer()
        elif menu == 4:
            listcustomer()
        elif menu == 0:
            print("Volviendo al menú principal.")
            return
        else:
            print("Opción no válida.")
        menu = 0  # Para mantener el ciclo activo hasta que decidan volver
