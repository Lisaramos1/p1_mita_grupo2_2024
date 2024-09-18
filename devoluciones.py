import funcionesvarias
import validaciones

def modicacion_de_estados(userid,nombrealbum,diccionariodiscos,matrizprestamos):
    cont=0
    print("Modicicación de estados \n")
    
    while cont<len(matrizprestamos): 
        if matrizprestamos[cont][0] == userid and matrizprestamos[cont][-1]==False: #Verificamos que el usuario tengo algun prestamo activo
            print(f"Fichero encontrado: {matrizprestamos[cont]},")
            print('Modificando estados... \n')
            matrizprestamos[cont][-1]=True
            
            for disco in diccionariodiscos:
                if nombrealbum.lower() == disco['nombre'].lower():
                    disco['cantidad'] += 1  # Incrementar la cantidad del disco existente
                    print(f"Stock actualizado: {disco} ")
             
            return 
        else :
            cont+=1
    print("carga terminada")


            