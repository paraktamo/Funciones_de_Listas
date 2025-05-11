from control.controlador import controlador_de_lista as es_lista
def eliminar(lista: list) -> int:
    """
    Elimina el ultimo elemento de la lista y lo retorna.
    Si esta vacia, no retorna nada.
    """
    if es_lista(lista) and lista != []:
        ultimo = lista[-1]
        lista [:] = lista[:-1]
        return ultimo
    else:
        print("Error en el ingreso de datos")
