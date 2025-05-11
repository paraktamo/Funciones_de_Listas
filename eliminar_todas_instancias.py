from control.controlador import controlador_de_lista as es_lista
def eliminar_todos(lista: list, elemento: int) -> list|None:
    """
    Busca los indices de los elementos iguales al elemento recibido.
    Los acumula en una lista y luego usa esa lista para recorrerla
    de derecha a izquierda eliminando todos esos elementos en la lista
    ingresada.
    Si no encuentra el elemento ingresado, retorna None.
    """
    if es_lista(lista) and lista != []:
        lista_acumuladora = []
        for i in range(len(lista)):
            if lista[i] == elemento:
                lista_acumuladora += [i]
        
        if lista_acumuladora != []:
            for i in range(len(lista_acumuladora)-1, -1, -1):
                    del lista[lista_acumuladora[i]]
            return lista
        else:
            print(f"No se encontraron coincidencias")
            return None
    else:
        print("Error en el ingreso de datos")