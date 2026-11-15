from abc import ABC, abstractmethod

from excepciones import DatoInvalidoError


# Clase base para los servicios de Software FJ
class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base, disponible=True):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None or not str(valor).strip():
            raise DatoInvalidoError(
                "El código del servicio no puede estar vacío."
            )

        self._codigo = str(valor).strip().upper()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalidoError(
                "El nombre del servicio no puede estar vacío."
            )

        self._nombre = valor.strip()

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):
        try:
            precio = float(valor)
        except (TypeError, ValueError) as error:
            raise DatoInvalidoError(
                "El precio base debe ser un valor numérico."
            ) from error

        if precio <= 0:
            raise DatoInvalidoError(
                "El precio base debe ser mayor que cero."
            )

        self._precio_base = precio

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        if not isinstance(valor, bool):
            raise DatoInvalidoError(
                "La disponibilidad debe ser True o False."
            )

        self._disponible = valor

    # Valida una duración recibida por los servicios
    def validar_duracion(self, duracion):
        try:
            valor = float(duracion)
        except (TypeError, ValueError) as error:
            raise DatoInvalidoError(
                "La duración debe ser un valor numérico."
            ) from error

        if valor <= 0:
            raise DatoInvalidoError(
                "La duración debe ser mayor que cero."
            )

        return valor

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass
