from cliente import Cliente
from servicio import Servicio
from reserva import Reserva
from excepciones import DatoInvalidoError


# Organiza los objetos del sistema en listas
class SistemaSoftwareFJ:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise DatoInvalidoError(
                "Solo se pueden registrar objetos Cliente."
            )

        if self.buscar_cliente(cliente.identificacion) is not None:
            raise DatoInvalidoError(
                "Ya existe un cliente con esa identificación."
            )

        self.clientes.append(cliente)

    def registrar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):
            raise DatoInvalidoError(
                "Solo se pueden registrar objetos Servicio."
            )

        if self.buscar_servicio(servicio.codigo) is not None:
            raise DatoInvalidoError(
                "Ya existe un servicio con ese código."
            )

        self.servicios.append(servicio)

    def registrar_reserva(self, reserva):
        if not isinstance(reserva, Reserva):
            raise DatoInvalidoError(
                "Solo se pueden registrar objetos Reserva."
            )

        if self.buscar_reserva(reserva.codigo) is not None:
            raise DatoInvalidoError(
                "Ya existe una reserva con ese código."
            )

        self.reservas.append(reserva)

    def buscar_cliente(self, identificacion):
        identificacion = str(identificacion).strip()

        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                return cliente

        return None

    def buscar_servicio(self, codigo):
        codigo = str(codigo).strip().upper()

        for servicio in self.servicios:
            if servicio.codigo == codigo:
                return servicio

        return None

    def buscar_reserva(self, codigo):
        codigo = str(codigo).strip().upper()

        for reserva in self.reservas:
            if reserva.codigo == codigo:
                return reserva

        return None

    def mostrar_resumen(self):
        return (
            f"Clientes registrados: {len(self.clientes)} | "
            f"Servicios registrados: {len(self.servicios)} | "
            f"Reservas registradas: {len(self.reservas)}"
        )
