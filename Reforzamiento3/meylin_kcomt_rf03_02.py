"""Crea un programa que calcule el Índice de Masa Corporal (IMC) de
una persona.
La fórmula es:

IMC : peso(kg) / altura (m)2
En el mensaje también indicar el nombre de la persona indicando su
IMC también
"""

# declara variables
nombre = "Meylin"
peso = float(65.2)
altura = float(1.50)
imc = peso / pow(altura,2)

#imprimir el mensaje
print(" El IMC de {} es de {:.2f}".format(nombre,imc))
