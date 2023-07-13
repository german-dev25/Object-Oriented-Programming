from view.languages import LANG_DICT


class ConsoleCommand:
    """
    Класс, представляющий команды для консольного интерфейса.

    :param language: Язык интерфейса.
    """

    def __init__(self, language):
        """
        Конструктор класса ConsoleCommand.

        :param language: Язык интерфейса.
        """
        command_values = LANG_DICT[language.lower()]['commands']
        self.ALL_READ = command_values[1]
        self.LIST_READ = command_values[2]
        self.DICT_READ = command_values[3]
        self.SEARCH = command_values[4]
        self.DELETE = command_values[5]
        self.EXIT = command_values[6]
