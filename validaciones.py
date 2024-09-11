
import re
import datetime


def SumadeDias(DiasdePrestamo):
    """
    Agregar:
    formato d/m
    """
    """
    pre: Se reciben los dias que se va a realizar el prestamo
    pos: Se devuelve la fecha de inicio del prestamo y la fecha de devolucion 
    """
    dia1=datetime.date.today()
    dia2=dia1+datetime.timedelta(DiasdePrestamo)
    
    dia1=str(dia1)
    dia2=str(dia2)
    
    return(dia1,dia2)
    
    
def existenciadeuser(userid,matriz):
    """
    Agregar: Funcionalidad.
    pre:Recibe el userid y la matriz
    pos:Si se encuetra el userdi== True ,, si no lo encuentra==False
    """
    for i in matriz :
        if matriz[0] == userid:
            return True
        else:
            return False

#def  DisponibilidadAlbum (album,matriz)

def ValidUsername (username):
    """
    pre: Recibe el username 
    pos: Valido=True ,, Invalido=False
    """
    patron='^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+.[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$'#Regex
    
    if re.match(patron,username):
        return True
    else:
        return False

def ValidUserid (userid):
    """
    pre: Recibe el userid 
    pos: Valido=True ,, Invalido=False
    """
    cad=str(userid)
    patron='[0-9]{4}'#regex
    if re.match(patron,cad):
        return True
    else : 
        return False