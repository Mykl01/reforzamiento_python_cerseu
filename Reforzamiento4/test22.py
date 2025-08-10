"""
4. Pedir al usuario que ingrese un nombre y apellidos
el cual será usada por un parámetro para una función que se creará e indicará cuantas letras tiene el nombre solamente.
 Usar la función un mínimo de dos veces para dos personas e indicar quien tiene el nombre con mayor número de caracteres (condicional)
"""

# Pedir el nombre y apellido (1er persona)
nom_completo1 = input("Ingrese el nombre y apellidos de la primera persona: ")
longitud_nombre1 = 0
for caracter in nom_completo1:
    if caracter == ' ':
        break
    longitud_nombre1 += 1

# Pedir el nombre y apellido (2da persona)
nombre_completo2 = input("Ingrese el nombre y apellidos de la segunda persona: ")
longitud_nombre2 = 0
for caracter in nombre_completo2:
    if caracter == ' ':
        break
    longitud_nombre2 += 1

# Print
print(f"\nEl primer nombre tiene {longitud_nombre1} letras.")
print(f"El segundo nombre tiene {longitud_nombre2} letras.")

# Comparar
if longitud_nombre1 > longitud_nombre2:
    print("El primer nombre es el más largo.")
elif longitud_nombre2 > longitud_nombre1:
    print("El segundo nombre es el más largo.")
else:
    print("Ambos nombres tienen la misma longitud.")