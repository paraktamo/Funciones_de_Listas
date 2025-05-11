from control.controlador import controlador_de_elemento as es_element, controlador_de_lista as es_lista
def vaciar_lista(lista: list) -> list:
    """
    Elimina todos los elementos de la lista.
    """
    if es_lista(lista) and lista != []:
        del lista[:]
        return lista
    else:
        print("Error en el ingreso de datos")