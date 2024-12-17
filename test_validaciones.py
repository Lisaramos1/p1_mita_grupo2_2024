import validaciones

def test_fecha_valida():
    assert validaciones.validaciondefecha("2024-10-05") == True

def test_fecha_invalida():
    assert validaciones.validaciondefecha("2024/10/05") == False

def test_username_valido():
    assert validaciones.ValidUsername("Martino") == True

def test_username_invalido():
    assert validaciones.ValidUsername("123") == False

def test_userid_valido():
    assert validaciones.ValidUserid(1234) == True

def test_userid_invalido():
    assert validaciones.ValidUserid(11) == False
