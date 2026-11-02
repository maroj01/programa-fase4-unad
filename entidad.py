from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError


# Clase base para las entidades que se van a manejar en el sistema
class Entidad(ABC):

    def __init__(self, identificacion):
        self.identificacion = identificacion

    # Permite consultar la identificacion
    @property
    def identificacion(self):
        return self._identificacion

    # Valida la identificacion antes de guardarla
    @identificacion.setter
    def identificacion(self, valor):

        # Se verifica que la identificacion no este vacia
        if valor is None or not str(valor).strip():
            raise DatoInvalidoError(
                "La identificación no puede estar vacía."
            )

        identificacion = str(valor).strip()

        # La identificacion solo debe contener numeros
        if not identificacion.isdigit():
            raise DatoInvalidoError(
                "La identificación debe contener únicamente números."
            )

        self._identificacion = identificacion

    # Cada clase que herede de Entidad debe implementar este metodo
    @abstractmethod
    def mostrar_informacion(self):
        pass
