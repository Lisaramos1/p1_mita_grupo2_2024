import funcionesvarias
import validaciones

def modicacion_de_estados(userid,nombrealbum,diccionariodiscos,matrizprestamos):
    cont=0
    
    while cont<len(matrizprestamos): 
        if matrizprestamos[cont][0] == userid and matrizprestamos[cont][-1]==False:
            print(f"Fichero encontrado: {matrizprestamos[cont]},")
            print('Modificando estados... \n')
            matrizprestamos[cont][-1]=True
            
            for disco in diccionariodiscos:
                if nombrealbum == disco['nombre']:
                    disco['cantidad'] += 1  # Incrementar la cantidad del disco existente
                    print(f"Disco actualizado: {disco} ")
            print() 
            return




            