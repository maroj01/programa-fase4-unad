# ==========================================
# CLASES DE EXCEPCIONES SOFTWARE FJ
# ==========================================

class SoftwareFJError(Exception):
    """Excepción base para los errores del sistema de Software FJ."""
    pass

class DatoInvalidoError(SoftwareFJError):
    """Se lanza ante datos inválidos, parámetros faltantes o inconsistencias."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza ante intentos de reserva incorrectos o servicios no disponibles."""
    pass