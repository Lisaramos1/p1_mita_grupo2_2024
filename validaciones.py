
import re
from datetime import datetime
from datetime import timedelta
from datetime import date

#Validaciones y transformaciones de formato fecha
def SumadeDias(DiasdePrestamo):
    """
    pre: Se reciben los dias que se va a realizar el prestamo
    pos: Se devuelve la fecha de inicio del prestamo y la fecha de devolucion 
    """
    dia1=date.today()
    dia2=dia1+timedelta(DiasdePrestamo)
    
    dia1=str(dia1)
    dia2=str(dia2)
    
    return(dia1,dia2)

def modificacionfechalimite(fecha,cantdediasdeprestamo):
    """
    pre: recibe la anterior fecha de devolición junto con la nueva cantidad de dias de prestamo
    pos: devulve la nueva fecha de devolución     
    """ 
    if cantdediasdeprestamo<=0: 
        print("La cantidad de dias debe ser valida")
        return False
    
    formato= "%Y-%m-%d"
    fecha_objeto = datetime.strptime(fecha,formato)
    nuevafechadevolucion=fecha_objeto + timedelta(cantdediasdeprestamo)
    
    aux=nuevafechadevolucion.date()
    
    nuevafechadevolucion=str(aux)
    return nuevafechadevolucion

def str_a_fecha(strfecha):
    formato= "%Y-%m-%d"
    fecha_objeto = datetime.strptime(strfecha,formato)
    aux=fecha_objeto.date()
    
    return aux
 
def existenciadeuser(userid,diccionariosdeusers):
    """
    pre:Recibe el userid y el diccionario
    pos:Si se encuetra el userdi== True , si no lo encuentra==False
    """
    if userid not in diccionariosdeusers:
        raise KeyError ("El usuario no fue registrado")
        return False
    else:
        return True
    

def existenciaprestamo (userid,matrizprestamos):
    cont=0
    while cont<len(matrizprestamos): 
        if matrizprestamos[cont][0] == userid:
            return True
        else:   
            cont+=1
    return False

#Validaciones regex
def validaciondefecha(fecha):
    """
    pre:recibe la fecha
    pos:si cumple los requerimientos = true , no cumple los requerimientos = false
    
    """
    patron='[0-9]{4}-[0-9]{2}-[0-9]{2}'
    if re.match(patron,fecha):
        return True
    else:
        return False
    

def ValidUsername (username):
    """
    pre: Recibe el username 
    pos: Valido=True ,, Invalido=False
    """
    patron= r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+.[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$' #Regex
    
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
