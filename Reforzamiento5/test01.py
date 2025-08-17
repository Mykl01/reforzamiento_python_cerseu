"""
Crear una clase Empleado que contenga los siguientes métodos, uno que
pida ingresar un nombre, apellido y edad, un método para pedir su sueldo
actual y otro método que lo imprima ambos resultados, pero estarán
contenidos en un diccionario. Comprobar los métodos instanciado la clase
respectivamente al menos para 3 empleados. Considerar en el constructor los
valores necesarios.
"""
class Empleado:
    def __init__(self):
        self.datos = {}
#metodo
    def ingresar_datos_personales(self):
        self.datos['nombre'] = input("Ingresar el nombre del empleado: ")
        self.datos['apellido'] = input("Ingresar el apellido del empleado: ")
        self.datos['edad'] = input("Ingresar la edad del empleado: ")

    def ingresar_sueldo_actual(self):
        self.datos['sueldo_actual'] = input("Ingresar el sueldo actual del empleado: ")

    def imprimir_resultados(self):
        for clave, valor in self.datos.items():
            print(f"{clave.capitalize().replace('_', ' ')}: {valor}")

# Validacion
if __name__ == "__main__":

    empleado1 = Empleado()
    empleado2 = Empleado()
    empleado3 = Empleado()

    print("Empleado 1")
    empleado1.ingresar_datos_personales()
    empleado1.ingresar_sueldo_actual()
    empleado1.imprimir_resultados()

    print("Empleado 2")
    empleado2.ingresar_datos_personales()
    empleado2.ingresar_sueldo_actual()
    empleado2.imprimir_resultados()

    print("Empleado 3")
    empleado3.ingresar_datos_personales()
    empleado3.ingresar_sueldo_actual()
    empleado3.imprimir_resultados()