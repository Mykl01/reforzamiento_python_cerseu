"""
Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado.
"""

# Diccionario inicial
persona = {
    'nombre': 'Juan Pérez',
    'edad': 35,
    'salario': 450000.00
}

print("Diccionario inicial:", persona)

# 1. Agregar el nuevo key "dni"
persona['dni'] = '06308954'
print("\nDiccionario después de agregar DNI:", persona)

# 2. Mostrar el salario y DNI
print(f"\nSalario: {persona['salario']}")
print(f"DNI: {persona['dni']}")

# 3. Eliminar el key "edad" y su valor
del persona['edad']

# 4. Mostrar el diccionario actualizado
print("\nDiccionario después de eliminar la edad:", persona)