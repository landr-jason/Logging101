import logging.config

output_filename = 'module.error.log'

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default_formatter': {
            'format': '[%(levelname)s:%(asctime)s] %(message)s'
        },
    },
    'handlers': {
        'module_file_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'default_formatter',
            'filename': output_filename
        },
    },
    'loggers': {
        __name__: {
            'handlers': ['module_file_handler'],
            'level': 'ERROR',
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)

def mock_function(prefix = None):
    if prefix is None:
        prefix = ''

    logger.debug(f"{prefix} MODULE DEBUG message")
    logger.info(f"{prefix} MODULE INFO message")
    logger.warning(f"{prefix} MODULE WARNING message")
    logger.error(f"{prefix} MODULE ERROR message")
    logger.critical(f"{prefix} MODULE CRITICAL message")

    return __name__, output_filename
