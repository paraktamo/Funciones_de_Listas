from control.controlador import controlador_de_lista as es_lista
def obtener_indice(lista: list, elemento: int) -> int:
    """
    Busca el elemento en la lista y retorna su indice.
    Si no lo encuentra retorna -1.
    """
    if es_lista(lista) and lista != []:
        flag = True
        for i in range(len(lista)):
            if lista[i] == elemento:
                print(f"El valor {elemento} está en la posición {i+1}")
                return i
            else:
                flag = False
        if flag == False:
            return -1
    else:
        print("Error en el ingreso de datos")
        return -1