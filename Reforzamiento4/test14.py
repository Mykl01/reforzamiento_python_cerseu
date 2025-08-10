"""
Crear una agenda basada en un diccionario donde los key serán los nombres de las personas y sus “values”
 serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso no exista
mostrar un mensaje de “No se encuentra registrado en la agenda”

"""
# Crear el diccionario
agenda = {}

# Ingresar el primer contacto
nombre1 = input("Ingrese el nombre de la persona: ").strip().capitalize()
numero1 = input(f"Ingrese el número de teléfono de {nombre1}: ")
agenda[nombre1] = numero1

# Ingresar el segundo contacto
nombre2 = input("Ingrese otro nombre de persona: ").strip().capitalize()
numero2 = input(f"Ingrese el número de teléfono de {nombre2}: ")
agenda[nombre2] = numero2

# Búsqueda de contactos
nombre_buscar = input("\nIngrese el nombre a buscar: ").strip().capitalize()

if nombre_buscar in agenda:
    print(f"El número de teléfono de {nombre_buscar} es: {agenda[nombre_buscar]}")
else:
    print(f"'{nombre_buscar}' no se encuentra registrado en la agenda.")

# Agenda actualizada
print("\n--- La Agenda actualizada es : {}".format(agenda))
