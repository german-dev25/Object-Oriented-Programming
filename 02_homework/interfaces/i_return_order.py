from abc import ABC, abstractmethod


class IReturnOrder(ABC):
    """
    Интерфейс, представляющий возврат товара в магазине.

    Methods:
        is_make_return() -> bool:
            Проверяет, возвращает ли покупатель товар.

        set_make_return(is_make_return: bool) -> None:
            Устанавливает флаг возврата товара для покупателя.

        is_have_returned() -> bool:
            Проверяет, вернул ли покупатель товар.

        set_have_returned(is_have_returned: bool) -> None:
            Устанавливает флаг успешного возврата товара для покупателя.
    """

    @abstractmethod
    def is_make_return(self) -> bool:
        """
        Проверяет, возвращает ли покупатель товар.

        :return :
            bool: Флаг, указывающий возвращает ли покупатель товар.
        """

    @abstractmethod
    def set_make_return(self, is_make_return: bool) -> None:
        """
        Устанавливает флаг возврата товара для покупателя.

        :arg :
            is_make_return (bool): Флаг, указывающий возвращает ли покупатель товар.

        :return :
            None
        """

    @abstractmethod
    def is_have_returned(self) -> bool:
        """
        Проверяет, вернул ли покупатель товар.

        :return :
            bool: Флаг, указывающий вернул ли покупатель товар.
        """

    @abstractmethod
    def set_have_returned(self, is_have_returned: bool) -> None:
        """
        Устанавливает флаг успешного возврата товара для покупателя.

        :arg :
            is_have_returned (bool): Флаг, указывающий вернул ли покупатель товар.

        :return :
            None
        """
