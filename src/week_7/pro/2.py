#фабрика декортаторов
import datetime
import inspect


def logging_decorator(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_args  = inspect.getcallargs(func, *args, **kwargs)
            run_date  = datetime.datetime.now()
            result = func(*args, **kwargs)
            inf = {
                "name":func.__name__,
                "arguments":func_args,
                "call_time":run_date,
                "result":result
            }
            logger.append(inf)
            return result
        return wrapper
    return decorator

logger = []  # этот словарь будет хранить наш "лог"

@logging_decorator(logger)  # в аргументы фабрики декораторов подается логгер
def test_simple(a, b=2):
    return 127

test_simple(1)  # при вызове функции в список logger должен добавиться словарь с
                # информацией о вызове функции

print(logger)