"""

6. Crear una clase PersonaPrestamo que hereda de la clase anterior (problema 5) donde tendrá los métodos: Uno,
que indicará si la persona está apta para un préstamo solo si ha estado más de 12 meses trabajando en la empresa en caso contrario se le
informa que no es posible darle el préstamo y la otra condición adicional es si su edad es mayor de 25 años.
Agregar un segundo método a esta nueva clase que te indicará si estás aprobado recibirás 10 veces tu sueldo de préstamo,
el total de préstamo otorgado es {cantidad_prestamo}.
Instanciar 3 veces la clase para mostrar diferentes resultados.
"""
class Persona:
    def __init__(self, nombre, edad, sueldo, meses_en_empresa):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.meses_en_empresa = meses_en_empresa

    def mostrar_datos_y_verificar_edad(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Sueldo: S/. {self.sueldo:.2f}")
        print(f"Meses en la empresa: {self.meses_en_empresa}")

        if self.edad >= 18:
            print("Estado: Es mayor de edad.")
        else:
            print("Estado: Es menor de edad.")

    def calcular_bonificacion(self):
        if self.edad >= 18:
            bonificacion = self.sueldo * 0.20
            return bonificacion
        else:
            return 0

    def mostrar_meses_trabajados(self):
        print(f"La persona {self.nombre} ha trabajado {self.meses_en_empresa} meses en la empresa.")


# --- Clase heredada de Persona ---
class PersonaPrestamo(Persona):
    def __init__(self, nombre, edad, sueldo, meses_en_empresa):
        super().__init__(nombre, edad, sueldo, meses_en_empresa)

    def apto_para_prestamo(self):

        if self.edad > 25 and self.meses_en_empresa > 12:
            print(f" {self.nombre}! Usted es apto para un préstamo.")
            return True
        else:
            print(f"{self.nombre}, no cumple con los requisitos para un préstamo.")
            return False

    def calcular_monto_prestamo(self):

        if self.apto_para_prestamo():
            cantidad_prestamo = self.sueldo * 10
            print(f"Aprobado: El total de préstamo otorgado es S/. {cantidad_prestamo:.2f}")
        else:
            print("No se otorga préstamo.")


#  Instanciando la clase PersonaPrestamo
# Caso 1: Apto para el préstamo
print("Caso 1: Ana (Apta)")
persona1 = PersonaPrestamo("Ana", 28, 3000, 15)
persona1.mostrar_datos_y_verificar_edad()
persona1.calcular_monto_prestamo()
print("\n" + "=" * 30 + "\n")

# Caso 2: No apto para el préstamo
print("Caso 2: Juan (No apto por edad)")
persona2 = PersonaPrestamo("Juan", 22, 2500, 20)
persona2.mostrar_datos_y_verificar_edad()
persona2.calcular_monto_prestamo()
print("\n" + "=" * 30 + "\n")

# Caso 3: No apto para el préstamo
print("Caso 3: Sofía (No apta por tiempo de trabajo)")
persona3 = PersonaPrestamo("Sofía", 30, 4000, 8)
persona3.mostrar_datos_y_verificar_edad()
persona3.calcular_monto_prestamo()
print("\n" + "=" * 30 + "\n")