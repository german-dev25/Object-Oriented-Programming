import logging

from logger.i_logger import ILogger


class LoggerFile(ILogger):
    """
    Класс LoggerFile представляет собой логгер для записи сообщений в файл.

    :param:
        log_file (str): Имя файла для записи лога.

    :methods:
        log_info(message: str) -> None:
            Метод для записи информационного сообщения в файл.

        log_warning(message: str) -> None:
            Метод для записи предупреждающего сообщения в файл.

        log_error(message: str) -> None:
            Метод для записи сообщения об ошибке в файл.

        log_debug(message: str) -> None:
            Метод для записи отладочного сообщения в файл.
    """
    def __init__(self,
                 log_file: str = 'app.log',
                 log_level: int = logging.DEBUG):
        self.logger = logging.getLogger('file_logger')
        self.logger.setLevel(log_level)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log_info(self, message: str) -> None:
        self.logger.info(message)

    def log_warning(self, message: str) -> None:
        self.logger.warning(message)

    def log_error(self, message: str) -> None:
        self.logger.error(message)

    def log_debug(self, message: str) -> None:
        self.logger.debug(message)
