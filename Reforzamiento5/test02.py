"""
Crear una clase llamada Circulo que contenga radio en su constructor y que contenga un método área que devuelva el área de un círculo.
Adicionalmente habrá un método que devuelva el perímetro del círculo.
También habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.14159

    def calcular_area(self):
        return self.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * self.pi * self.radio

    def pedir_radio(self):

        try:
            nuevo_radio = float(input("Ingresar el radio del círculo: "))
            self.radio = nuevo_radio
            print("El radio ha sido actualizado a: {}".format(self.radio))
        except ValueError:
            print("La entrada no es válida. Por favor, ingresar un número.")

# Instancia 1: Círculo con radio inicial de 5
circulo1 = Circulo(5)
print("Círculo 1")
print(f"Radio inicial: {circulo1.radio}")
print(f"Área: {circulo1.calcular_area():.2f}")
print(f"Perímetro: {circulo1.calcular_perimetro():.2f}")

# Instancia 2: Círculo con radio inicial de 12.5
circulo2 = Circulo(12.5)
print("Círculo 2")
print(f"Radio inicial: {circulo2.radio}")
print(f"Área: {circulo2.calcular_area():.2f}")
print(f"Perímetro: {circulo2.calcular_perimetro():.2f}")

# mostrar los nuevos resultados
print("Círculo 1 Actualizado")
circulo1.pedir_radio()
print(f"Área actualizada: {circulo1.calcular_area():.2f}")
print(f"Perímetro actualizado: {circulo1.calcular_perimetro():.2f}")