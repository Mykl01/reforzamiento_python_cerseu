"""
5. Crear una función que aceptará por parámetro dos valores que serán ingresados por el usuario,
una lista donde los valores serán llenados por el usuario también
y un segundo parámetro que eliminará de la lista que fue ingresada a la función,
finalmente el output de la función será la lista actualizada sin el valor que se sacará de la lista.
Mostrar también la lista original y el número que fue eliminado.
"""
# Lista
lista = []
cant_elementos = int(input("¿Cuántos elementos quiere ingresar en la lista?: "))

for i in range(cant_elementos):
    elemento = input(f"Ingresar el elemento {i + 1}: ")
    lista.append(elemento)

# Pedir al usuario el valor a eliminar
valor_eliminar = input("Ingresar el valor que desea eliminar de la lista: ")

# Eliminar un valor

print("Lista inicial:", lista)

if valor_eliminar in lista:
    lista.remove(valor_eliminar)
    print(f"Se eliminó el valor: {valor_eliminar}")
else:
    print(f"El valor '{valor_eliminar}' no se encontró en la lista.")

# print lista
print("Lista actualizada:", lista)