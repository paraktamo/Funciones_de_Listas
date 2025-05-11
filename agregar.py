from control.controlador import controlador_de_lista as es_lista
def agregar(lista: list, elemento) -> list: 
    """
        Modifica la lista original, añadiendo elemento como su ultimo elemento.
        Retorna la lista modificada.
    """
    if es_lista(lista):
        lista += [elemento]
        return lista
    else:
        print("Error en el ingreso de datos")