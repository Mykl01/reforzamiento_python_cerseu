"""
Crear un programa que cuente cuántas veces aparece cada vocal en la oración. Ignorar mayúsculas/minúsculas
Input: “Programación en Python”
Output:
a: 2
e: 1
i: 1
o: 2
u: 0
Métodos útiles: lower() y count()
"""

frase = "Programación en Python"

# frase a minúsculas
frase_minusculas = frase.lower()

# diccionario para contar las vocales
conteo_vocales = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

# contar cada vocal
conteo_vocales['a'] = frase_minusculas.count('a')
conteo_vocales['e'] = frase_minusculas.count('e')
conteo_vocales['i'] = frase_minusculas.count('i')
conteo_vocales['o'] = frase_minusculas.count('o')
conteo_vocales['u'] = frase_minusculas.count('u')

# resultados del conteo de vocales
print("Conteo de vocales:")
print(f"a: {conteo_vocales['a']}")
print(f"e: {conteo_vocales['e']}")
print(f"i: {conteo_vocales['i']}")
print(f"o: {conteo_vocales['o']}")
print(f"u: {conteo_vocales['u']}")