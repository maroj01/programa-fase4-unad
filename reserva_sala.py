from servicio import Servicio
from excepciones import DatoInvalidoError, ReservaInvalidaError


# Servicio para reservar salas por horas
class ReservaSala(Servicio):

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        capacidad,
        ubicacion,
        disponible=True
    ):
        super().__init__(
            codigo,
            nombre,
            precio_base,
            disponible
        )

        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.validar_parametros()

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor):
        try:
            capacidad = int(valor)
        except (TypeError, ValueError) as error:
            raise DatoInvalidoError(
                "La capacidad debe ser un número entero."
            ) from error

        if capacidad <= 0:
            raise DatoInvalidoError(
                "La capacidad debe ser mayor que cero."
            )

        self._capacidad = capacidad

    @property
    def ubicacion(self):
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalidoError(
                "La ubicación de la sala no puede estar vacía."
            )

        self._ubicacion = valor.strip()

    def validar_parametros(self):
        if not self.disponible:
            raise ReservaInvalidaError(
                "La sala no está disponible."
            )

        return True

    def calcular_costo(self, duracion):
        if not self.disponible:
            raise ReservaInvalidaError(
                "No se puede reservar una sala no disponible."
            )

        horas = self.validar_duracion(duracion)
        costo = self.precio_base * horas

        # Las salas grandes tienen un recargo
        if self.capacidad > 20:
            costo *= 1.10

        return round(costo, 2)

    def describir(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Sala: {self.nombre} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Ubicación: {self.ubicacion} | "
            f"Estado: {estado}"
        )
