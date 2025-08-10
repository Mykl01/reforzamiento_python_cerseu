"""
Strings:
1.
Dada una frase u oración encontrar que palabra es la que tiene más caracteres y cuántos caracteres tiene
Input: “La programación en Python es poderosa”
Output: “programación” – 12 caracteres
"""

frase = "La programación en Python es poderosa"

# variables
palabra_larga = ""
palabra_actual = ""

for caracter in frase:
    if caracter != ' ':
        palabra_actual += caracter
    else:
        if len(palabra_actual) > len(palabra_larga):
            palabra_larga = palabra_actual
        palabra_actual = ""

if len(palabra_actual) > len(palabra_larga):
    palabra_larga = palabra_actual

#  resultado output
print(f'"{palabra_larga}" - {len(palabra_larga)} caracteres')