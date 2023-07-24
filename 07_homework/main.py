from calculator.calculator import Calculator
from calculator.calculator_deco import CalculatorDeco
from calculator.i_calculator import ICalculator
from calculator.controller_calculator import ControllerCalculator
from logger.i_logger import ILogger
from logger.logger_console import LoggerConsole
from logger.logger_file import LoggerFile


# инициализируем калькулятор,
# логгер (консольный или файловый),
# экземпляр калькулятора с логированием
def run():
    calculator_old: ICalculator = Calculator()
    logger: ILogger = LoggerFile()
    # logger: ILogger = LoggerConsole()
    calculator_deco: ICalculator = CalculatorDeco(calculator_old, logger)
    controller: ControllerCalculator = ControllerCalculator(
        calculator=calculator_deco)

    controller()


if __name__ == "__main__":
    run()
