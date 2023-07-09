from domen.person import Person, N


class Teacher(Person):
    """
    Класс, представляющий учителя.

    Наследуется от класса Person.

    :param first_name: Имя учителя.
    :param age: Возраст учителя.
    :param acad_degree: Ученая степень учителя (необязательный).

    :methods:
        __init__(first_name: str, age: N, acad_degree: str = None):
            Инициализация объекта класса Teacher.

    """

    def __init__(self, first_name: str, age: N, acad_degree: str = None):
        """
        Инициализация объекта класса Teacher.

        :param first_name: Имя учителя.
        :param age: Возраст учителя.
        :param acad_degree: Ученая степень учителя (необязательный).
        """
        super().__init__(first_name, age)
        self.acad_degree = acad_degree
