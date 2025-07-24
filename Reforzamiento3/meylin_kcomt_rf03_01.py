"""
Escribe un programa que convierta cierta cantidad de soles a dólares,
usando un tipo de cambio que se proporciona en el programa.
Estos valores estarán dentro de sus variables respectivamente.
La salida mostrará tres cambios que hagas respectivamente de tres
montos a convertir.
"""

# declaracion de variables
tipo_de_cambio = 3.55

print("El Tipo de cambio actual (1 dólar USD): S/ {:.2f}".format(tipo_de_cambio))

# salidas

# Salida 1
monto_soles_1 = 50
cambio_dolares_monto_1 = monto_soles_1 / tipo_de_cambio
print("S/ {:.2f} equivalen a US$ {:.2f}".format(monto_soles_1,cambio_dolares_monto_1))

# Salida 2
monto_soles_2 = 100
cambio_dolares_monto_2 = monto_soles_2 / tipo_de_cambio
print("S/ {:.2f} equivalen a US$ {:.2f}".format(monto_soles_2,cambio_dolares_monto_2))

# Salida 3
monto_soles_3 = 200
cambio_dolares_monto_3 = monto_soles_3 / tipo_de_cambio
print("S/ {:.2f} equivalen a US$ {:.2f}".format(monto_soles_3,cambio_dolares_monto_3))