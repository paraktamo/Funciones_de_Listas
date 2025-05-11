from control.controlador import controlador_de_elemento as es_element, controlador_de_lista as es_lista
def insertar(lista: list, elemento: int, indice: int) -> list:
    """
    Ingresa un valor en el indice especificado y retorna la lista modificada
    """
    if es_lista(lista) and es_element(indice):
        lista[:] = lista[:indice] + [elemento] + lista[indice:]
        return lista
    else:
        print("Error en el ingreso de datos")