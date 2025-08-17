"""
Crear una clase Alumno que tenga como atributos el nombre, edad y la nota final del alumno.
Crear los métodos para inicializar sus atributos, otro para imprimirlos y un método para mostrar un mensaje con el resultado de la nota,
si ha aprobado (mayor o igual a 13) o no el alumno.
Instanciar la clase por lo menos 4 veces (4 alumnos)
"""

class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota Final: {self.nota_final}")

    def mostrar_resultado(self):

        if self.nota_final >= 13:
            print(f"{self.nombre} ha aprobado el curso.")
        else:
            print(f"{self.nombre} no ha aprobado el curso")

#Instanciando
alumno1 = Alumno("Ana", 20, 14)
alumno2 = Alumno("Pedro", 22, 10)
alumno3 = Alumno("Sofía", 19, 17)
alumno4 = Alumno("Luis", 21, 19)

#Mostrando los datos y resultados
print("Alumno 1")
alumno1.imprimir_datos()
alumno1.mostrar_resultado()

print("Alumno 2")
alumno2.imprimir_datos()
alumno2.mostrar_resultado()

print("Alumno 3")
alumno3.imprimir_datos()
alumno3.mostrar_resultado()

print("Alumno 4")
alumno4.imprimir_datos()
alumno4.mostrar_resultado()