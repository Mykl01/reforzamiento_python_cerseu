"""
1. Pedir dos números positivos mediante terminal al usuario.
Mostrar como salida el número cuya sumatoria de dígitos es el mayor y los números cuya sumatoria de dígitos es menor que 10.
Utilizar una o más funciones, según sea conveniente.
"""

# 2 números positivos
num1 = int(input("Ingrese el primer número positivo: "))
num2 = int(input("Ingrese el segundo número positivo: "))

# Suma de los dígitos del primer número
suma1 = 0
temp_num1 = num1
while temp_num1 > 0:
    suma1 += temp_num1 % 10
    temp_num1 //= 10

# Suma de los dígitos del segundo número
suma2 = 0
temp_num2 = num2
while temp_num2 > 0:
    suma2 += temp_num2 % 10
    temp_num2 //= 10

# Resultado
if suma1 > suma2:
    print(f"El número con la mayor sumatoria de dígitos es: {num1} (suma = {suma1})")
elif suma2 > suma1:
    print(f"El número con la mayor sumatoria de dígitos es: {num2} (suma = {suma2})")
else:
    print(f"Ambos números tienen la misma sumatoria de dígitos: {suma1}")

# Suma es menor que 10
encontrado = False
if suma1 < 10:
    print(f"- {num1} (suma = {suma1})")
    encontrado = True
if suma2 < 10:
    print(f"- {num2} (suma = {suma2})")
    encontrado = True
if not encontrado:
    print("Ninguno de los números tiene una sumatoria de dígitos menor que 10.")