# Задание 1! Разобраться в работе декоратора functools.wraps
from functools import wraps
import logging


def bib_1(func):
    @wraps(func)
    def wrapper():
        print("Фантастика,\n Комедия,\n Детектив.")
        return func()
    return wrapper


@bib_1
def genres():
    """Жанры"""


print(genres.__name__)
print(genres.__doc__)


# Задание 2! Создать декоратор, который будет логировать поведение функции. Записывать действия и сохранять в файл.
def log(func):

    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        # Создаем файл логов для записи
        fh = logging.FileHandler("list.log")
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        result = func(*args, **kwargs)
        logger.info("Result %s" % result)
        return result
    return wrap_log


@log
def my_random(a):
    """a + random digit"""
    import random
    r = random.randint(0, 100)
    return a + r


if __name__ == "__main__":
    value = my_random(12)   # a = 12
    print(value)
