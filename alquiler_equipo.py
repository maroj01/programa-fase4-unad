from servicio import Servicio
from excepciones import DatoInvalidoError, ReservaInvalidaError


# Servicio para alquilar equipos tecnológicos
class AlquilerEquipo(Servicio):

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        cantidad_disponible,
        tipo_equipo,
        disponible=True
    ):
        super().__init__(
            codigo,
            nombre,
            precio_base,
            disponible
        )

        self.cantidad_disponible = cantidad_disponible
        self.tipo_equipo = tipo_equipo
        self.validar_parametros()

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self, valor):
        try:
            cantidad = int(valor)
        except (TypeError, ValueError) as error:
            raise DatoInvalidoError(
                "La cantidad disponible debe ser un número entero."
            ) from error

        if cantidad < 0:
            raise DatoInvalidoError(
                "La cantidad disponible no puede ser negativa."
            )

        self._cantidad_disponible = cantidad

    @property
    def tipo_equipo(self):
        return self._tipo_equipo

    @tipo_equipo.setter
    def tipo_equipo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalidoError(
                "El tipo de equipo no puede estar vacío."
            )

        self._tipo_equipo = valor.strip()

    def validar_parametros(self):
        if not self.disponible or self.cantidad_disponible == 0:
            raise ReservaInvalidaError(
                "El equipo no está disponible."
            )

        return True

    def calcular_costo(self, duracion, cantidad=1):
        if not self.disponible:
            raise ReservaInvalidaError(
                "No se puede alquilar un equipo no disponible."
            )

        horas = self.validar_duracion(duracion)

        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError) as error:
            raise DatoInvalidoError(
                "La cantidad solicitada debe ser un número entero."
            ) from error

        if cantidad <= 0:
            raise DatoInvalidoError(
                "La cantidad solicitada debe ser mayor que cero."
            )

        if cantidad > self.cantidad_disponible:
            raise ReservaInvalidaError(
                "No hay suficientes equipos disponibles."
            )

        costo = self.precio_base * horas * cantidad

        # Se aplica un descuento para alquileres largos
        if horas >= 8:
            costo *= 0.95

        return round(costo, 2)

    def describir(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Equipo: {self.nombre} | "
            f"Tipo: {self.tipo_equipo} | "
            f"Cantidad disponible: {self.cantidad_disponible} | "
            f"Estado: {estado}"
        )
