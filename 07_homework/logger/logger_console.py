import logging

from logger.i_logger import ILogger


class LoggerConsole(ILogger):
    """
    Класс LoggerConsole представляет собой логгер для записи сообщений в консоль.

    :methods:
        log_info(message: str) -> None:
            Метод для записи информационного сообщения в консоль.

        log_warning(message: str) -> None:
            Метод для записи предупреждающего сообщения в консоль.

        log_error(message: str) -> None:
            Метод для записи сообщения об ошибке в консоль.

        log_debug(message: str) -> None:
            Метод для записи отладочного сообщения в консоль.
    """
    def __init__(self, log_level=logging.DEBUG):
        self.logger = logging.getLogger('console_logger')
        self.logger.setLevel(log_level)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

    def log_info(self, message: str) -> None:
        self.logger.info(message)

    def log_warning(self, message: str) -> None:
        self.logger.warning(message)

    def log_error(self, message: str) -> None:
        self.logger.error(message)

    def log_debug(self, message: str) -> None:
        self.logger.debug(message)
