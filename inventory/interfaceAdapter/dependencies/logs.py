import logging
from logging.handlers import TimedRotatingFileHandler

import os

# Configurar la carpeta de logs
if not os.path.exists('logs'):
    os.makedirs('logs')

def logs_register(log_name):
    # Crear el formateador
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')

    # Configurar TimedRotatingFileHandler
    log_handler = TimedRotatingFileHandler(
        filename=f'logs/{log_name}.log',
        when='D',   # Rotación diaria
        interval=1, # Cada día
        backupCount=7  # Número de archivos de respaldo
    )
    log_handler.setFormatter(log_formatter)

    # Crear el logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)  # Nivel de log
    logger.addHandler(log_handler)  # Añadir el handler al logger
    
    return logger

# Inicializar el logger
logger = logs_register('inventory_logs')