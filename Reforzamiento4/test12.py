"""
Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario.

"""
# Crear diccionario
cubos = {}

# Pedir al usuario
print("Por favor, ingresa 4 números:")

for i in range(4):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    #el cubo del número
    cubo = numero ** 3
    # Agregar el número
    cubos[numero] = cubo

# print el diccionario final
print("\n--- Diccionario de números y sus cubos ---")
print(cubos)