"""
Crear un diccionario con 6 departamentos del país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.

- Comprobar que no existe este departamento borrado dentro del
diccionario.
"""

# Crear diccionario con 6 departamentos
deptos = {
    1: 'Lima',
    2: 'Arequipa',
    3: 'Cusco',
    4: 'Puno',
    5: 'Ica',
    6: 'La Libertad'
}
print("Diccionario inicial:{}".format( deptos))

# Borrar un departamento
del deptos[4]
print("Diccionario después de borrar 'Puno':", deptos)

# Actualizar el penúltimo departamento
deptos[5] = 'Huánuco'
print("Diccionario después de actualizar 'Ica' por 'Huánuco':", deptos)

# valida que el depto borrado no existe en el diccionario
depto_borrado = 'Puno'
if depto_borrado not in deptos.values():
    print(f"Correcto: '{depto_borrado}' no se encuentra en el diccionario.")
else:
    print(f"Error: '{depto_borrado}' aún se encuentra en el diccionario.")

print("Diccionario final actualizado:", deptos)