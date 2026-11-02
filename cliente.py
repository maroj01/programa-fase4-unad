import re

from entidad import Entidad
from excepciones import DatoInvalidoError


# Clase para manejar los datos de los clientes
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):
        # Se envia la identificacion a la clase Entidad
        super().__init__(identificacion)

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # Permite consultar el nombre
    @property
    def nombre(self):
        return self._nombre

    # Valida el nombre antes de guardarlo
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalidoError(
                "El nombre del cliente no puede estar vacío."
            )

        nombre = valor.strip()

        if len(nombre) < 3:
            raise DatoInvalidoError(
                "El nombre debe contener al menos 3 caracteres."
            )

        self._nombre = nombre

    # Permite consultar el correo
    @property
    def correo(self):
        return self._correo

    # Valida que el correo tenga un formato correcto
    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalidoError(
                "El correo no puede estar vacío."
            )

        correo = valor.strip()

        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(patron, correo):
            raise DatoInvalidoError(
                "El correo electrónico no tiene un formato válido."
            )

        self._correo = correo.lower()

    # Permite consultar el telefono
    @property
    def telefono(self):
        return self._telefono

    # Valida el telefono antes de guardarlo
    @telefono.setter
    def telefono(self, valor):
        if valor is None or not str(valor).strip():
            raise DatoInvalidoError(
                "El teléfono no puede estar vacío."
            )

        telefono = str(valor).strip()

        if not telefono.isdigit():
            raise DatoInvalidoError(
                "El teléfono debe contener únicamente números."
            )

        if len(telefono) != 10:
            raise DatoInvalidoError(
                "El teléfono debe contener 10 dígitos."
            )

        self._telefono = telefono

    # Muestra los datos principales del cliente
    def mostrar_informacion(self):
        return (
            f"Cliente: {self.nombre} | "
            f"Identificación: {self.identificacion} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )
