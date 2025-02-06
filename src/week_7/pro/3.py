from functools import lru_cache
import inspect
import time
import datetime

def cache_results(func):
    cache_dict  = {}
    def wrapper(*args, **kwargs):
        func_args  = inspect.getcallargs(func, *args,**kwargs)
        key_name = f"{func.__name__}({func_args})"
        if key_name not in cache_dict:
            start  = datetime.datetime.now()
            func_res  = func(*args, **kwargs)
            end = datetime.datetime.now()
            print(f"Выполнено за {end.second - start.second} секунды")
            cache_dict[key_name] = func_res
            return func_res
        else:
            print("Результат взят из кэша")
            return cache_dict[key_name]
    return wrapper

@cache_results
def slow_function(x):
    time.sleep(2)  # Симулируем долгую обработку
    return x * 2

result = slow_function(25)
# Вывод: Выполнено за 2 секунды

print(result)  # Вывод: 625


result2 = slow_function(25)
# Вывод: Результат взят из кэша

print(result2)  # Вывод: 625