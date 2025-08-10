"""
Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado
insertados en la terminal

"""

lista_vacia = []
lista_vacia.append(1)
lista_vacia.append(2)
lista_vacia.append(3)
lista_vacia.append(4)
lista_vacia.append(5)
lista_vacia.append(6)
lista_vacia.append(7)
lista_vacia.append(8)
lista_vacia.append(9)
lista_vacia.append(10)
print(f"{lista_vacia}")

suma = sum(lista_vacia)
print("Esta es la suma de la lista: {}".format(suma))

media = suma / len(lista_vacia)
print("La media es :{}".format(media))