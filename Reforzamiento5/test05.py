"""
Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una persona. Implementar los métodos necesarios para inicializar los atributos (constructor),
 un método para mostrar los datos e indicar si la persona es mayor de edad o no y otro método que bonificación que retornará el 20% adicional de su sueldo,
 en caso sea mayor de edad. Un método para saber cuántos meses ha estado trabajando en la empresa
Instanciar por lo menos la clase con 3 diferentes personas.
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
            print("Es mayor de edad.")
        else:
            print("Es menor de edad.")

    def calcular_bonificacion(self):

        if self.edad >= 18:
            bonificacion = self.sueldo * 0.20
            return bonificacion
        else:
            return 0

    def mostrar_meses_trabajados(self):

        print(f"La persona {self.nombre} ha trabajado {self.meses_en_empresa} meses en la empresa.")


# --- Instanciando la clase Persona para 3 individuos ---

# Persona 1: Mayor de edad con sueldo
persona1 = Persona("Ana", 25, 3000, 18)
print("Persona 1")
persona1.mostrar_datos_y_verificar_edad()
bonificacion_ana = persona1.calcular_bonificacion()
print(f"Bonificación: S/. {bonificacion_ana:.2f}")
persona1.mostrar_meses_trabajados()

# Persona 2: Menor de edad
persona2 = Persona("Carlos", 17, 1500, 5)
print("Persona 2")
persona2.mostrar_datos_y_verificar_edad()
bonificacion_carlos = persona2.calcular_bonificacion()
print(f"Bonificación: S/. {bonificacion_carlos:.2f}")
persona2.mostrar_meses_trabajados()

# Persona 3: Mayor de edad con otro sueldo
persona3 = Persona("Sofía", 30, 5000, 36)
print("Persona 3")
persona3.mostrar_datos_y_verificar_edad()
bonificacion_sofia = persona3.calcular_bonificacion()
print(f"Bonificación: S/. {bonificacion_sofia:.2f}")
persona3.mostrar_meses_trabajados()