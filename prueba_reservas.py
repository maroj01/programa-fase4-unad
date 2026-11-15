import logging

import logger

from cliente import Cliente
from reserva_sala import ReservaSala
from reserva import Reserva
from sistema import SistemaSoftwareFJ
from excepciones import (
    DatoInvalidoError,
    ReservaInvalidaError
)


print("=== PRUEBAS DE RESERVAS SOFTWARE FJ ===")

sistema = SistemaSoftwareFJ()


# Se crean los objetos necesarios
try:
    cliente = Cliente(
        "1020399333",
        "Andres Espinosa",
        "andres@gmail.com",
        "3001234567"
    )

    sala = ReservaSala(
        "SAL-001",
        "Sala de conferencias",
        50000,
        20,
        "Piso 2"
    )

    sistema.registrar_cliente(cliente)
    sistema.registrar_servicio(sala)

except (DatoInvalidoError, ReservaInvalidaError) as error:
    print(f"Error al preparar las pruebas: {error}")
    logging.error(f"Error al preparar las pruebas: {error}")


# Prueba 12: crear y confirmar reserva
try:
    reserva = Reserva(
        "RES-001",
        cliente,
        sala,
        3
    )

    sistema.registrar_reserva(reserva)
    reserva.confirmar()

except (DatoInvalidoError, ReservaInvalidaError) as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al confirmar reserva: {error}")

else:
    print("\nReserva confirmada correctamente")
    print(reserva.mostrar_resumen())

finally:
    print("Prueba 12 finalizada")


# Prueba 13: confirmar dos veces
try:
    reserva.confirmar()

except ReservaInvalidaError as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al confirmar reserva: {error}")

finally:
    print("Prueba 13 finalizada")


# Prueba 14: cancelar reserva
try:
    reserva.cancelar()

except ReservaInvalidaError as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al cancelar reserva: {error}")

else:
    print("\nReserva cancelada correctamente")
    print(f"Estado actual: {reserva.estado}")

finally:
    print("Prueba 14 finalizada")


# Prueba 15: cancelar dos veces
try:
    reserva.cancelar()

except ReservaInvalidaError as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al cancelar reserva: {error}")

finally:
    print("Prueba 15 finalizada")


# Prueba 16: reserva con duración incorrecta
try:
    reserva_invalida = Reserva(
        "RES-002",
        cliente,
        sala,
        "tres horas"
    )

except DatoInvalidoError as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al crear reserva: {error}")

    if error.__cause__ is not None:
        print(
            "Causa original:",
            type(error.__cause__).__name__
        )

finally:
    print("Prueba 16 finalizada")


print("\n" + sistema.mostrar_resumen())
print("\n=== FIN DE LAS PRUEBAS DE RESERVAS ===")
