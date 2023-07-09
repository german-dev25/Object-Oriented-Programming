from domen.person import Person


class Student(Person):
    """
    Класс, представляющий студента.

    Наследуется от абстрактного класса Person.

    :attr :
        name (str): Имя студента.
        age (int): Возраст студента.
        student_id (int): Идентификатор студента.

    :methods :
        get_student_id() -> int:
            Возвращает идентификатор студента.

        set_student_id(student_id: int):
            Устанавливает идентификатор студента.

        __lt__(o: 'Student'):
            Переопределенный метод сравнения для оператора `<`.
            Сравнивает студентов по возрасту и идентификатору.

        __str__() -> str:
            Возвращает строковое представление студента.
            Формат строки: "Student [name=<имя>, age=<возраст>, id=<идентификатор>]"
    """

    def __init__(self, name: str, age: int, student_id: int):
        """
        Конструктор класса Студент
        :param: name (str): Имя студента.
        :param: age (int): Возраст студента.
        :param: student_id (int): Идентификатор студента.
        """
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_id(self) -> int:
        """
        Возвращает идентификатор студента.

        :return :
            int: Идентификатор студента.
        """
        return self.student_id

    def set_student_id(self, student_id: int):
        """
        Устанавливает идентификатор студента.

        :arg :
            student_id (int): Идентификатор студента.
        """
        self.student_id = student_id

    def __lt__(self, o: 'Student'):
        """
        Переопределенный метод сравнения для оператора `<`.
        Сравнивает студентов по возрасту и идентификатору.
        Используется по определению в методе sorted.

        :arg :
            o (Student): Другой студент для сравнения.

        :return :
            bool: True, если текущий студент младше по age или меньше по id
            другого студента, False в противном случае.
        """
        if self.get_age() == o.get_age():
            return self.student_id < o.student_id
        return self.get_age() < o.get_age()

    def __str__(self) -> str:
        """
        Возвращает строковое представление студента.

        :return :
            str: Строковое представление студента.
            Формат строки: "Student [name=<имя>, age=<возраст>, id=<идентификатор>]"
        """
        return f'{type(self).__name__} ' \
               f'[name={self.name}, age={self.age}, id={self.student_id}]'
