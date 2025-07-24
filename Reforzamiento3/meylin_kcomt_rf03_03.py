"""
Escribe un programa que reciba dos flotantes, luego estos pasarán a
ser convertidos en enteros. Indique si el primero es múltiplo del
segundo. Usar mod para la verificación si el residuo es 0
"""

num1 = float(50.0)
num2 = float(20.5)

# Convertir los números flotantes a enteros

num1_entero = int(num1)
num2_entero = int(num2)

#validacion
if num2_entero == 0:
    print("\nNo se puede verificar si el segundo numero es cero.")
else:
    if num1_entero % num2_entero == 0:
        print("\n el numero entero  {} es múltiplo de {}.".format(num1_entero,num2_entero))
    else:
        print("\n el numero entero {} NO es múltiplo de {}".format(num1_entero,num2_entero))

