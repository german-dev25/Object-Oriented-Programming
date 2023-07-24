from abc import ABC, abstractmethod


class ILogger(ABC):
    """
    Абстрактный класс ILogger представляет интерфейс для логгера.

    :methods:
        log_info(msg: str) -> None:
            Абстрактный метод для записи информационного сообщения.

        log_warning(msg: str) -> None:
            Абстрактный метод для записи предупреждающего сообщения.

        log_error(msg: str) -> None:
            Абстрактный метод для записи сообщения об ошибке.

        log_debug(msg: str) -> None:
            Абстрактный метод для записи отладочного сообщения.
    """
    @abstractmethod
    def log_info(self, msg: str): pass

    @abstractmethod
    def log_warning(self, msg: str): pass

    @abstractmethod
    def log_error(self, msg: str): pass

    @abstractmethod
    def log_debug(self, msg: str): pass