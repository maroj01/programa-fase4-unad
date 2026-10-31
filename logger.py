import logging
from excepciones import DatoInvalidoError, ReservaInvalidaError

logging.basicConfig(
    filename='registro_eventos.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)