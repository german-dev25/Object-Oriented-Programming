from domen.person import Person, N


class Employee(Person):
    """
    Класс, представляющий работника.

    Наследуется от класса Person.

    :attr :
        name (str): Имя работника.
        age (N): Возраст работника.
        special (str, optional): Должность работника.

    :methods :
        __init__(first_name: str, age: N, special: str = None):
            Конструктор класса Работник.

        __str__() -> str:
            Возвращает строковое представление работника.
            Формат строки: "Employee [name=<имя>, age=<возраст>,
            special=<должность>]"
    """

    def __init__(self, first_name: str, age: N, special: str = None):
        """
        Конструктор класса Работник.

        :param: first_name (str): Имя работника.
        :param: age (N): Возраст работника.
        :param: special (str, optional): Должность работника.
        """
        super().__init__(name=first_name, age=age)
        self.special = special

    def __str__(self) -> str:
        """
        Возвращает строковое представление работника.

        :return :
            str: Строковое представление работника.
            Формат строки:
            "Employee [name=<имя>, age=<возраст>, special=<должность>]"
        """
        return f'{type(self).__name__} ' \
               f'[name={self.name}, age={self.age}, special={self.special}]'
