"""
Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista.
"""

#lista con 6 departamentos
deptos = ["Lima", "Arequipa", "Cusco", "Puno", "Ica", "La Libertad"]
print("Lista original:", deptos)

#pedir ingresar un nuevo depto
depto_a_sustituir = input("Ingrese el departamento que desea sustituir (debe estar en la lista): ")
nuevo_depto = input("Ingrese el nuevo departamento: ")

#verifica si el depto esta en la lista y sustituir
if depto_a_sustituir in deptos:
    indice = deptos.index(depto_a_sustituir)
    deptos[indice] = nuevo_depto
    print("El departamento", depto_a_sustituir, "ha sido sustituido por", nuevo_depto)
    print("Nueva lista:", deptos)
else:
    print("El departamento ingresado para sustituir no se encuentra en la lista.")
    print("La lista no ha sido modificada:", deptos)