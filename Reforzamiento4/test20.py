"""
2. Crea una función que al ingresar dos números por parámetro mostrará todos los cuadrados de los números que hay entre ellos
 (Usar la función una vez y mostrar el resultado por consola). Los números serán ingresados y solicitados al usuario.
"""

# Pedir los números
num1 = int(input("Ingresar el primer número: "))
num2 = int(input("Ingresar el segundo número: "))

# Determinar el rango de números
if num1 <= num2:
    inicio = num1
    fin = num2
else:
    inicio = num2
    fin = num1

print(f"\nCuadrados de los números entre {inicio} y {fin}:")

# Iterar y mostrar el cuadrado de cada número en el rango
for numero in range(inicio, fin + 1):
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")