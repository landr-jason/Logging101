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
        'file_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'default_formatter',
            'filename': output_filename
        },
    },
    'loggers': {
        __name__: {
            'handlers': ['file_handler'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)

def mock_function():
    logger.debug("module debug test")
    logger.info("module info test")
    logger.warning("module warning test")
    logger.error("module error test")
    logger.critical("module critical test")

    return __name__, output_filename
