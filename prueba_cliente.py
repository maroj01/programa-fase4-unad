import logging

# Importa la configuracion del archivo de logs
import logger

from cliente import Cliente
from excepciones import DatoInvalidoError


print("=== PRUEBAS DE CLIENTES SOFTWARE FJ ===")


# Prueba 1: cliente con datos correctos
try:
    cliente1 = Cliente(
        "1234567890",
        "Andres Espinosa",
        "andres@gmail.com",
        "3001234567"
    )

except DatoInvalidoError as error:
    print(f"Error: {error}")
    logging.error(f"Error al registrar cliente: {error}")

else:
    print("\nCliente registrado correctamente")
    print(cliente1.mostrar_informacion())
    logging.info("Cliente registrado correctamente")

finally:
    print("Prueba 1 finalizada")


# Prueba 2: cliente con nombre vacio
try:
    cliente2 = Cliente(
        "9876543210",
        "",
        "cliente@gmail.com",
        "3109876543"
    )

except DatoInvalidoError as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al registrar cliente: {error}")

finally:
    print("Prueba 2 finalizada")


# Prueba 3: cliente con correo incorrecto
try:
    cliente3 = Cliente(
        "1112223334",
        "Carlos Perez",
        "correo_incorrecto",
        "3151234567"
    )

except DatoInvalidoError as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al registrar cliente: {error}")

finally:
    print("Prueba 3 finalizada")


# Prueba 4: cliente con telefono incorrecto
try:
    cliente4 = Cliente(
        "2223334445",
        "Laura Gomez",
        "laura@gmail.com",
        "123"
    )

except DatoInvalidoError as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al registrar cliente: {error}")

finally:
    print("Prueba 4 finalizada")


# Prueba 5: identificacion con letras
try:
    cliente5 = Cliente(
        "ABC123",
        "Pedro Ramirez",
        "pedro@gmail.com",
        "3201234567"
    )

except DatoInvalidoError as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al registrar cliente: {error}")

finally:
    print("Prueba 5 finalizada")


print("\n=== FIN DE LAS PRUEBAS ===")
