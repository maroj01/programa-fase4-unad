from servicio import Servicio
from excepciones import DatoInvalidoError, ReservaInvalidaError


# Servicio para asesorías en áreas tecnológicas
class AsesoriaEspecializada(Servicio):

    ESPECIALIDADES_VALIDAS = [
        "Redes",
        "Fibra óptica",
        "Ciberseguridad",
        "IoT",
        "Computación en la nube"
    ]

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        especialidad,
        asesor,
        disponible=True
    ):
        super().__init__(
            codigo,
            nombre,
            precio_base,
            disponible
        )

        self.especialidad = especialidad
        self.asesor = asesor
        self.validar_parametros()

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalidoError(
                "La especialidad no puede estar vacía."
            )

        especialidad_encontrada = None

        for especialidad in self.ESPECIALIDADES_VALIDAS:
            if especialidad.lower() == valor.strip().lower():
                especialidad_encontrada = especialidad
                break

        if especialidad_encontrada is None:
            opciones = ", ".join(self.ESPECIALIDADES_VALIDAS)

            raise DatoInvalidoError(
                f"La especialidad no es válida. Opciones: {opciones}."
            )

        self._especialidad = especialidad_encontrada

    @property
    def asesor(self):
        return self._asesor

    @asesor.setter
    def asesor(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalidoError(
                "El nombre del asesor no puede estar vacío."
            )

        self._asesor = valor.strip()

    def validar_parametros(self):
        if not self.disponible:
            raise ReservaInvalidaError(
                "La asesoría no está disponible."
            )

        return True

    def calcular_costo(self, duracion):
        if not self.disponible:
            raise ReservaInvalidaError(
                "No se puede solicitar una asesoría no disponible."
            )

        horas = self.validar_duracion(duracion)
        costo = self.precio_base * horas

        # Ciberseguridad tiene un recargo por especialización
        if self.especialidad == "Ciberseguridad":
            costo *= 1.15

        return round(costo, 2)

    def describir(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Asesoría: {self.nombre} | "
            f"Especialidad: {self.especialidad} | "
            f"Asesor: {self.asesor} | "
            f"Estado: {estado}"
        )
