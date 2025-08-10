"""
Escribir un programa donde ingresarás el tamaño de la lista mediante consola, este tamaño servirá para ingresar una cantidad X
 de nombres de alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de la lista que fueron ingresados
"""
# Tamano de la lista
tamano_lista = int(input("Ingresar el tamaño de la lista de alumnos: "))

lista_alum = []
print(f"Ahora ingresar los {tamano_lista} nombres de los alumnos:")
for i in range(tamano_lista):
    nombre = input(f"Ingresar el nombre del alumno {i + 1}: ")
    lista_alum.append(nombre)

#print resultados
print("El tamaño de la lista es:", len(lista_alum))
print("Los nombres de los alumnos ingresados son:", lista_alum)
