"""
3. Crear una función que sume los dígitos del número ingresado y muestre por consola la suma de todos estos dígitos.
"""
# Pedir un número
numero = int(input("Ingresar un número para sumar sus dígitos: "))

# Inicializar la suma
suma = 0

if numero < 0:
    numero = -numero

while numero > 0:
    digito = numero % 10
    suma += digito
    numero //= 10

# Print resultado
print(f"La suma de los dígitos del número es: {suma}")