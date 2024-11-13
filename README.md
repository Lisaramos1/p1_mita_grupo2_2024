# Proyecto-F-Pr1
Proyecto PLAM
Este software es un sistema de gestión para el alquiler de discos de vinilo, con tres módulos CRUD principales. Las funcionalidades básicas incluyen:
-Gestión de usuarios: Permite agregar, modificar, eliminar y consultar usuarios registrados en el sistema.
-Gestión de discos: Facilita la administración del catálogo de discos de vinilo, con opciones para agregar, editar, eliminar y listar los discos disponibles.
-Gestión de préstamos: Proporciona la funcionalidad para gestionar el alquiler de discos, incluyendo el registro de nuevos préstamos, devoluciones, y control de disponibilidad de los discos.
El objetivo del sistema es optimizar y simplificar la administración del inventario y las transacciones de préstamo de vinilos.




Descripcción estructura de Datos
Proyecto final de programacion 1 biblioteca de discos 
Se necesitaran como minimo 3 tablas
Stock: PKA¹ , Artista , Nombre , Genero
Usuarios: PKU² , DNI , Nombre , Telefono y Domicilio
Prestamos: (PKA , PKU)³ , Fechaini , Fechafin , Monto,Estado de devolucion
Programado en python Visual Studio Code





¹PKU: Primary key album (utilizado para diferenciar entre los productos)
²PKU: Primary key Usuario (Utilizado para diferenciar entre los usuarios, no esta definido aun puede ser el CUIL o un autonumber generico)
³(PKA , PKU): Primary key compuesta por dos primary key donde se deberia tener almacenado los datos de album y usuario



{'id':1,'nombre':'Disco 1','Artista':A,'Genero':Rock,'cantidad':5}
