import logging

import logger

from cliente import Cliente
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada
from reserva import Reserva
from sistema import SistemaSoftwareFJ
from excepciones import SoftwareFJError


def ejecutar_sistema():
    print("======================================")
    print("       SISTEMA SOFTWARE FJ")
    print("======================================")

    sistema = SistemaSoftwareFJ()

    try:
        cliente = Cliente(
            "1020399333",
            "Andres Espinosa",
            "andres@gmail.com",
            "3001234567"
        )

        sala = ReservaSala(
            "SAL-001",
            "Sala principal",
            50000,
            25,
            "Piso 2"
        )

        equipo = AlquilerEquipo(
            "EQU-001",
            "Router empresarial",
            20000,
            5,
            "Equipo de red"
        )

        asesoria = AsesoriaEspecializada(
            "ASE-001",
            "Diseño de infraestructura",
            80000,
            "Redes",
            "María Torres"
        )

        sistema.registrar_cliente(cliente)
        sistema.registrar_servicio(sala)
        sistema.registrar_servicio(equipo)
        sistema.registrar_servicio(asesoria)

        reserva = Reserva(
            "RES-001",
            cliente,
            sala,
            3
        )

        sistema.registrar_reserva(reserva)
        reserva.confirmar()

    except SoftwareFJError as error:
        print(f"\nError controlado: {error}")
        logging.error(f"Error en la ejecución principal: {error}")

    else:
        print("\nOperación realizada correctamente")
        print(reserva.mostrar_resumen())

        print("\nServicios registrados:")

        for servicio in sistema.servicios:
            print("-", servicio.describir())

        logging.info(
            "Ejecución principal finalizada correctamente"
        )

    finally:
        print("\n" + sistema.mostrar_resumen())
        print("\n=== EJECUCIÓN FINALIZADA ===")


if __name__ == "__main__":
    ejecutar_sistema()
