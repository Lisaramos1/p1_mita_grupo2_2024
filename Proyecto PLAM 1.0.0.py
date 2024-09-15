import DiscosStock
import prestamos
import Usuarios

def menu_usuarios(): 
    while True:
        print('1. ➕ Agregar Usuario')
        print('2. ⚙ Modificar Usuario')
        print('3. ❌ Eliminar Usuario')
        print('4. 👀 Mostrar la lista de Usuarios')
        print('0.  Volver')
        menu = input('¿Qué desea hacer?: ')

        if menu == '1':
            # Input desde el main para agregar cliente
            nombreapellido = input("Ingrese el nombre y apellido: ")
            dni = input("Ingrese el DNI sin puntos ni espacios: ")
            Usuarios.addcustomer(nombreapellido, dni)  
        elif menu == '2':
            # Input desde el main para modificar cliente
            dni = input("Ingrese el DNI de la persona a modificar: ")
            nuevo_nya = input("Ingrese el nuevo nombre y apellido: ")
            Usuarios.modcustomer(dni, nuevo_nya)  
        elif menu == '3':
            # Input desde el main para eliminar cliente
            dni = input("Ingrese el DNI de la persona a eliminar: ")
            Usuarios.delcustomer(dni)  
        elif menu == '4':
            Usuarios.listcustomer()  
        elif menu == '0':
            print("Volviendo al menú principal.")
            return
        else:
            print("Opción no válida.")

# Menú principal del programa
uso = 0
while uso == 0:
    print('1. 🎶 Discos')
    print('2. 👥 Usuarios')
    print('3. 📚 Prestamos')
    print('0. 🚪 Salir')
    
    funcion = input('Seleccione una opción: ')

    if funcion == '1':
        DiscosStock.menudiscos()  # Llamada al menu de discos
    elif funcion == '2':
        menu_usuarios()  # Llamada al menu de usuarios
    elif funcion == '3':
        prestamos.crud_prestamos()  # Llamada al menu de préstamos)
    elif funcion == '0':
        print("Saliendo del programa...")
        uso = 1  # Salir del programa
    else:
        print("Opción no válida. Intente de nuevo.")
