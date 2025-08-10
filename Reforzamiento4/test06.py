"""6. Tiene una lista de invitados que llegaron a una boda de acuerdo a su orden
de llegada:
guests = [“Ana”, “Katherine”, “Pedro”, “Luis”, “Raúl”, “Fiorella”, “Miguel”]
Se requiere reorganizar esta lista.
Primero los que tienen número impar y en el orden que fueron llegando
Segundo las personas que tienen número par de letras
Input: [“Ana”, “Pedro”, “Raúl”, “Fiorella”, “Katherine”, “Miguel”, “Luis”]
Output: [“Ana”, “Pedro”, ”Katherine”, “Raúl”, “Fiorella”, “Miguel”, “Luis”]
"""

guests = ["Ana", "Katherine", "Pedro", "Luis", "Raúl", "Fiorella", "Miguel"]

# impar y par
impares = []
pares = []

for nombre in guests:
  if len(nombre) % 2 != 0:
    impares.append(nombre)
  else:
    pares.append(nombre)

# Concatenar las listas para obtener la nueva lista reorganizada
nueva_guests = impares + pares

# Imprimir el resultado
print("Lista original:", guests)
print("Lista reorganizada:", nueva_guests)