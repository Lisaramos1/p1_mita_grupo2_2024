def generadorid (matriz):
    """
    pre: recibe una matriz
    pos: Devuelve el numero de id mediante el len de la lista
    """
    len_lista=len(matriz)
    id=f"{len_lista:04}"
    return id 