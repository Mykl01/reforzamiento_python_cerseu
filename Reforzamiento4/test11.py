"""
5. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u
"""

# Crear un diccionario con algunos datos iniciales
diccionario = {
    'nombre': 'Lucho',
    'salario': 2500,
    'departamento': 'TI'
}

# 1. Ingresar la carrera en el diccionario
carrera = input("Ingresa el nombre de tu carrera: ")
diccionario['carrera'] = carrera

# 2. Asignar los nombres y la carrera
nombre_estudiante = diccionario['nombre']
carrera_estudiante = diccionario['carrera']

print(f"\nEl nombre del estudiante es: {nombre_estudiante}")
print(f"El nombre de la carrera es: {carrera_estudiante}")
print("\nDiccionario  actualizado:", diccionario)