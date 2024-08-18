import sys
from typing import Callable, Any

def log(filename:str=None) -> Callable:
    """Декоратор для логирования работы функций"""
    def decorator(func:Callable) -> Callable:
        """ Декоратор, который оборачивает функцию для логирования её выполнения"""
        def wrapper(*args:Any, **kwargs:Any) -> Any:
            """Обёртка, которая выполняет функцию и логирует её выполнение"""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
            except Exception as e:
                result = None
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"

            if filename:
                with open(filename, "a") as file:
                    file.write(log_message)
            print(log_message, file=sys.stdout)

            return result

        return wrapper

    return decorator
