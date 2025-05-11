from agregar import agregar
from insertar import insertar
from obtener_indice import obtener_indice
from eliminar_ultimo import eliminar
from eliminar_primera_instancia import eliminar_primer_instancia
from eliminar_todas_instancias import eliminar_todos
from vaciar_lista import vaciar_lista

lista_prueba = [0, 1, 9, 2, 3, 4, 9, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

insertar(lista_prueba, 16, 1)
print(lista_prueba)

obtener_indice(lista_prueba, 6)
print(lista_prueba)

eliminar(lista_prueba)
print(lista_prueba)

eliminar_primer_instancia(lista_prueba, 16)
print(lista_prueba)

eliminar_todos(lista_prueba, 16)
print(lista_prueba)

vaciar_lista(lista_prueba)
print(lista_prueba)

agregar(lista_prueba, 16)
print(lista_prueba)