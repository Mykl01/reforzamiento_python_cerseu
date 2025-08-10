"""
7. Realizar un programa donde se ingresarán por consola los nombres de los alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso y las notas de c/u. Guardarás la información en un diccionario donde las claves serán los nombres de c/u de estos alumnos y sus valores serán las notas de esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a “Pedro tiene la nota de 15” y también la media de todas las notas.

"""
# Pedir la cantidad de alumnos
cant_alum = int(input("Ingrese la cantidad de alumnos: "))

# Crear un diccionario - alumnos y sus notas
alum_notas = {}

# Ingresar los nombres y notas de cada alumno
for i in range(cant_alum):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    alum_notas[nombre] = nota

# 1. print los alumnos con sus notas
print("\n--- Notas de los alumnos ---")
for nombre, nota in alum_notas.items():
    print(f"{nombre} tiene la nota de {nota}")

# 2. Calcular la media
if alum_notas:  # Asegurarse de que el diccionario no esté vacío
    suma_notas = sum(alum_notas.values())
    media_notas = suma_notas / len(alum_notas)
    print(f"\nLa nota media de todos los alumnos es: {media_notas:.2f}") 
else:
    print("\nNo se ingresaron notas para calcular la media.")