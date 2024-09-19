# main.py
import logging
from logging_config import setup_logging
from my_package import module1, module2
from database import db_module
from helpers import helper_module

logger = logging.getLogger(__name__)

def main():
    setup_logging()  # This sets up logging for the entire project
    logger.info("This is a log message from main.py before the modules run")
    module1.do_something()
    module2.do_something_else()
    db_module.write_to_db()
    helper_module.generate_something()

if __name__ == "__main__":
    main()
