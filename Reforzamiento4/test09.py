"""
Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tienes.

"""

# Diccionario inicial
persona = {
    'nombre': 'Juan',
    'edad': 35,
    'ciudad': 'Lima'
}

# Convertir los pares clave-valor a una lista de duplas
lista_persona = list(persona.items())

# Mostrar la lista resultante
print("La lista resultante es: {}".format(lista_persona))

# Mostrar el tipo de datos de la variable final
print("El tipo de datos de la nueva variable es:", type(lista_persona))