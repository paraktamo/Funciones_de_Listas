from control.controlador import controlador_de_lista as es_lista
def eliminar_primer_instancia(lista: list, elemento: int) -> int:
    """
    Elimina la primera ocurrencia de un elemento en la lista y lo retorna.
    Si no lo encuentra retorna None.
    """
    if es_lista(lista) and lista != []:
        flag = True
        for i in range(len(lista)):
            if lista[i] == elemento:
                del lista[i]
                print (f"De la lista se quitó el valor {elemento} de la posición {i+1}")
                return elemento
            else:
                flag = False
        if flag == False:
            return None
    else:
        print("Error en el ingreso de datos")

eliminar_primer_instancia([], 1)
