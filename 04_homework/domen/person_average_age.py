from domen.person_comparator import P
from typing import List


class AverageAge:
    """
    Класс AverageAge используется для подсчета среднего возраста списка объектов.

    :methods:
        average_ages(persons_list: List[P]) -> None:
            Статический метод для подсчета среднего возраста объектов в списке.

            :param persons_list (List[P]): Список объектов, для которых нужно
            подсчитать средний возраст.
            :return: None
    """
    @staticmethod
    def average_ages(persons_list: List[P]) -> None:
        """
        Подсчитывает средний возраст объектов в списке и выводит его в консоль.

        :param persons_list: Список объектов, для которых нужно подсчитать
        средний возраст.
        :type persons_list: List[P]
        :return: None
        """
        total_age = sum(person.get_age() for person in persons_list)
        average_age = total_age / len(persons_list)
        print("{:.2f}".format(average_age))
