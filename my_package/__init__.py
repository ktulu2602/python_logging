# my_package/__init__.py
from logging_config import setup_logging

# Ensure logging is set up when the package is imported
setup_logging()

# Optionally, you can get the logger for the package
import logging
logger = logging.getLogger(__name__)

logger.debug("Logging is set up for my_package")
