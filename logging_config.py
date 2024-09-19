# logging_config.py
import logging
import logging.config

def setup_logging(file_log_level: str = 'INFO', stream_log_level: str = 'DEBUG'):
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': stream_log_level,
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': 'app.log',
                'level': file_log_level,
            },
        },
        'root': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    }

    logging.config.dictConfig(logging_config)
