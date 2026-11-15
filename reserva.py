import logging

from cliente import Cliente
from servicio import Servicio
from excepciones import DatoInvalidoError, ReservaInvalidaError


# Relaciona un cliente con un servicio
class Reserva:

    ESTADOS_VALIDOS = [
        "pendiente",
        "confirmada",
        "cancelada"
    ]

    def __init__(
        self,
        codigo,
        cliente,
        servicio,
        duracion,
        cantidad=1
    ):
        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.cantidad = cantidad
        self.estado = "pendiente"

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None or not str(valor).strip():
            raise DatoInvalidoError(
                "El código de la reserva no puede estar vacío."
            )

        self._codigo = str(valor).strip().upper()

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if not isinstance(valor, Cliente):
            raise ReservaInvalidaError(
                "La reserva debe tener un cliente válido."
            )

        self._cliente = valor

    @property
    def servicio(self):
        return self._servicio

    @servicio.setter
    def servicio(self, valor):
        if not isinstance(valor, Servicio):
            raise ReservaInvalidaError(
                "La reserva debe tener un servicio válido."
            )

        self._servicio = valor

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        try:
            duracion = float(valor)
        except (TypeError, ValueError) as error:
            raise DatoInvalidoError(
                "La duración de la reserva debe ser numérica."
            ) from error

        if duracion <= 0:
            raise DatoInvalidoError(
                "La duración debe ser mayor que cero."
            )

        self._duracion = duracion

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        try:
            cantidad = int(valor)
        except (TypeError, ValueError) as error:
            raise DatoInvalidoError(
                "La cantidad debe ser un número entero."
            ) from error

        if cantidad <= 0:
            raise DatoInvalidoError(
                "La cantidad debe ser mayor que cero."
            )

        self._cantidad = cantidad

    def calcular_total(self):
        # AlquilerEquipo acepta una cantidad adicional
        if self.servicio.__class__.__name__ == "AlquilerEquipo":
            return self.servicio.calcular_costo(
                self.duracion,
                self.cantidad
            )

        return self.servicio.calcular_costo(self.duracion)

    def confirmar(self):
        if self.estado == "confirmada":
            raise ReservaInvalidaError(
                "La reserva ya se encuentra confirmada."
            )

        if self.estado == "cancelada":
            raise ReservaInvalidaError(
                "No se puede confirmar una reserva cancelada."
            )

        if not self.servicio.disponible:
            raise ReservaInvalidaError(
                "El servicio no está disponible."
            )

        self.estado = "confirmada"

        logging.info(
            f"Reserva {self.codigo} confirmada correctamente"
        )

    def cancelar(self):
        if self.estado == "cancelada":
            raise ReservaInvalidaError(
                "La reserva ya se encuentra cancelada."
            )

        self.estado = "cancelada"

        logging.info(
            f"Reserva {self.codigo} cancelada correctamente"
        )

    def mostrar_resumen(self):
        total = self.calcular_total()

        return (
            f"Reserva: {self.codigo} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} horas | "
            f"Estado: {self.estado} | "
            f"Total: ${total:,.2f}"
        )
