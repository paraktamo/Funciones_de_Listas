# Instancia de control de datos ingresados
def controlador_de_lista (lista):
    if type(lista) == list:
        return True
    else:
        return False
    
def controlador_de_elemento (elemento):
    if type(elemento) == int or type(elemento) == float:
        return True
    else:
        return False