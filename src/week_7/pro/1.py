import datetime
import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start  = datetime.datetime.now()
        result  = func(*args, **kwargs)
        end = datetime.datetime.now()
        print(end.second - start.second)
        return result
    return wrapper


@time_decorator
def sleep_1_sec():
    time.sleep(1)
    print("function")
    return 25

result  = sleep_1_sec()
print(result)