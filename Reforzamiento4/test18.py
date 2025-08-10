"""
3.
Pide al usuario que ingrese una frase y una palabra, obtén si la palabra está dentro de la oración sin importar si está en mayúsculas o minúsculas.
En caso que aparezca, indica la posición del primer carácter en donde empieza
Input: frase = “Python y sus enormes ventajas”, palabra = “Python”
Output: “Python aparece en la posición 0”
Métodos útiles: lower() y find()
"""
# Ingresar una frase y una palabra
frase = input("Ingresar una frase: ")
palabra = input("Ingresar una palabra para buscar: ")

frase_min = frase.lower()
palabra_min = palabra.lower()

# Busqueda
encontrado = False
posicion = -1

# Encontrar la palabra
for i in range(len(frase_min) - len(palabra_min) + 1):
    if frase_min[i:i + len(palabra_min)] == palabra_min:
        encontrado = True
        posicion = i
        break

# El resultado
if encontrado:
    print(f"'{palabra}' aparece en la posición {posicion}")
else:
    print(f"'{palabra}' no se encontró en la frase.")