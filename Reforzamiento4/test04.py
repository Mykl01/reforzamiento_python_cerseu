"""
Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola.
"""

estudiantes = ["Luis","Maria","Juan","Jose","Marta"]
nuevo_estudiante = input("Ingrese Nuevo estudiante")

#validar si el nombre esta en la lista inicial de estudiantes
if nuevo_estudiante in estudiantes:
    estudiantes.remove(nuevo_estudiante)
    print(f"'{nuevo_estudiante}' ha sido eliminado de la lista.")
else:
    print(f"'{nuevo_estudiante}' no se encuentra en la lista. Se agregará.")
    estudiantes.append(nuevo_estudiante)

# print la lista actualizada
print("Lista de estudiantes actualizada:{}".format(estudiantes))