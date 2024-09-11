import re 

# Función para validar DNI 
def validar_dni(dni):
    return re.fullmatch('\\d{7,8}', dni) is not None

# Lista de los clientes
customer = []

# Función para agregar clientes
def addcustomer():
    nombre = input("Ingrese el nombre: ").capitalize()  # Capitaliza el nombre
    apellido = input("Ingrese el apellido: ").capitalize()
    dni = input("Ingrese el DNI sin puntos ni espacios: ")

    # Validación del DNI
    if not validar_dni(dni):
        print("DNI inválido. Debe contener entre 7 y 8 dígitos sin puntos ni espacios.")
        return
    
    newcustomer = {"nombre": nombre, "apellido": apellido, "dni": dni}
    customer.append(newcustomer)
    print(f"Cliente {nombre} {apellido} agregado exitosamente.")
    
def modcustomer():
    dni = input("Ingrese el DNI de la persona a modificar: ")
    
    # Búsqueda del cliente con el DNI
    for persona in customer:
        if persona["dni"] == dni:
            nuevo_nombre = input("Ingrese el nuevo nombre: ").capitalize()
            nuevo_apellido = input("Ingrese el nuevo apellido: ").capitalize()
            persona["nombre"] = nuevo_nombre
            persona["apellido"] = nuevo_apellido
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
            print(f"Nombre: {persona['nombre']} - Apellido: {persona['apellido']} - DNI: {persona['dni']}")

# Función principal del menú
def menue():
    while True:
        print('1 Agregar persona')
        print('2 Modificar persona')
        print('3 Eliminar persona')
        print('4 Mostrar la lista de personas')
        print('0 Volver')
        menu = input('¿Qué desea hacer?: ')

        if menu == '1':
            addcustomer()
        elif menu == '2':
            modcustomer()
        elif menu == '3':
            delcustomer()
        elif menu == '4':
            listcustomer()
        elif menu == '0':
            print("Volviendo al menú principal.")
            return
        else:
            print("Opción no válida.")
        menu = 0  # Para mantener el ciclo activo hasta que decidan volver
menue()