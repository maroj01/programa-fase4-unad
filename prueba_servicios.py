import logging

# Carga la configuración del archivo de registro
import logger

from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada
from excepciones import DatoInvalidoError, ReservaInvalidaError


print("=== PRUEBAS DE SERVICIOS SOFTWARE FJ ===")


# Prueba 6: reserva de sala válida
try:
    sala = ReservaSala(
        "SAL-001",
        "Sala de conferencias",
        50000,
        25,
        "Piso 2"
    )

    costo_sala = sala.calcular_costo(3)

except (DatoInvalidoError, ReservaInvalidaError) as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al crear la sala: {error}")

else:
    print("\nSala creada correctamente")
    print(sala.describir())
    print(f"Costo por 3 horas: ${costo_sala:,.2f}")
    logging.info("Reserva de sala calculada correctamente")

finally:
    print("Prueba 6 finalizada")


# Prueba 7: sala con capacidad inválida
try:
    sala_invalida = ReservaSala(
        "SAL-002",
        "Sala de capacitación",
        40000,
        -5,
        "Piso 1"
    )

except (DatoInvalidoError, ReservaInvalidaError) as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al crear la sala: {error}")

finally:
    print("Prueba 7 finalizada")


# Prueba 8: alquiler de equipo válido
try:
    equipo = AlquilerEquipo(
        "EQU-001",
        "Router empresarial",
        20000,
        5,
        "Equipo de red"
    )

    costo_equipo = equipo.calcular_costo(4, 2)

except (DatoInvalidoError, ReservaInvalidaError) as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al alquilar equipo: {error}")

else:
    print("\nEquipo alquilado correctamente")
    print(equipo.describir())
    print(f"Costo del alquiler: ${costo_equipo:,.2f}")
    logging.info("Alquiler de equipo calculado correctamente")

finally:
    print("Prueba 8 finalizada")


# Prueba 9: equipo no disponible
try:
    equipo_no_disponible = AlquilerEquipo(
        "EQU-002",
        "Analizador de red",
        30000,
        0,
        "Medición",
        False
    )

except (DatoInvalidoError, ReservaInvalidaError) as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al alquilar equipo: {error}")

finally:
    print("Prueba 9 finalizada")


# Prueba 10: asesoría válida
try:
    asesoria = AsesoriaEspecializada(
        "ASE-001",
        "Diseño de red empresarial",
        80000,
        "Redes",
        "María Torres"
    )

    costo_asesoria = asesoria.calcular_costo(2)

except (DatoInvalidoError, ReservaInvalidaError) as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error al crear asesoría: {error}")

else:
    print("\nAsesoría creada correctamente")
    print(asesoria.describir())
    print(f"Costo de la asesoría: ${costo_asesoria:,.2f}")
    logging.info("Asesoría calculada correctamente")

finally:
    print("Prueba 10 finalizada")


# Prueba 11: duración no numérica
try:
    asesoria.calcular_costo("dos horas")

except DatoInvalidoError as error:
    print(f"\nError controlado: {error}")
    logging.error(f"Error en duración de asesoría: {error}")

    if error.__cause__ is not None:
        print(
            "Causa original:",
            type(error.__cause__).__name__
        )

finally:
    print("Prueba 11 finalizada")


# Prueba de polimorfismo
print("\n=== DESCRIPCIÓN POLIMÓRFICA ===")

servicios = [sala, equipo, asesoria]

for servicio in servicios:
    print(servicio.describir())


print("\n=== FIN DE LAS PRUEBAS DE SERVICIOS ===")
