import logging

from app.utils.paths import LOGS_DIR

APP_LOG = LOGS_DIR / "app.log"
ERROR_LOG = LOGS_DIR / "errors.log"


class Logger:

    @staticmethod
    def setup():
        """
        Configure application loggers.
        """

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.FileHandler(
                    APP_LOG,
                    encoding="utf-8"
                ),
                logging.StreamHandler()
            ]
        )

        error_handler = logging.FileHandler(
            ERROR_LOG,
            encoding="utf-8"
        )

        error_handler.setLevel(
            logging.ERROR
        )

        logging.getLogger().addHandler(
            error_handler
        )

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

    @staticmethod
    def error(message):
        logging.error(message)