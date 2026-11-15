from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError


class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base, disponible=True):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass
