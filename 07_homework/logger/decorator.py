from typing import Callable, Any


def log_method(func: Callable) -> Callable:
    def wrapped(self, *args, **kwargs) -> Any:
        self.logger.log_info(f"Calling method: {func.__name__}. ")
        result = func(self, *args, **kwargs)
        self.logger.log_info(
            f"Result: {self.old_calc.get_result()} "
            f"(Type: {type(self.old_calc.get_result()).__name__})")
        return result

    return wrapped
