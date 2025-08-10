"""
Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura “00054”
y su value será el coste de la factura.
El programa tendrá la opción de pedir nueva factura (por consola) que se agregará al diccionario.
Cada vez que el área de contabilidad pague una factura se pedirá el número de factura que fue cancelada, si existe mostrar
un mensaje donde indicará “La factura ya está cancelada” caso contrario “El número de factura no existe”
Considerar que cada vez que se realice algún pago o ingreso de una nueva factura se mostrará inmediatamente al diccionario actualizado.

"""
# Diccionario de facturas pendientes
facturas_pendientes = {
    '00054': 1500.00,
    '00055': 200.50,
    '00056': 75.25
}
# Diccionario  facturas canceladas
facturas_canceladas = {}

print("Facturas iniciales:", facturas_pendientes)

# Agregar una nueva factura
print("\nAgregar nueva factura")
num_nueva_factura = input("Ingrese el número de la nueva factura: ")
coste_nueva_factura = float(input(f"Ingrese el coste de la factura {num_nueva_factura}: "))
facturas_pendientes[num_nueva_factura] = coste_nueva_factura
print(f"Factura {num_nueva_factura} agregada correctamente.")
print("Diccionario actualizado:", facturas_pendientes)

# Pagar una factura
print("\n Pagar una factura")
num_factura_a_pagar = input("Ingrese el número de la factura que fue pagada: ")

# Verificar si la factura ya fue cancelada
if num_factura_a_pagar in facturas_canceladas:
    print("La factura ya está cancelada.")
elif num_factura_a_pagar in facturas_pendientes:
    # Mover la factura de pendientes a canceladas
    coste_factura = facturas_pendientes.pop(num_factura_a_pagar)
    facturas_canceladas[num_factura_a_pagar] = coste_factura
    print(f"La factura {num_factura_a_pagar} ha sido pagada.")
else:
    print("El número de factura no existe.")


print("Facturas pendientes:", facturas_pendientes)
print("Facturas canceladas:", facturas_canceladas)