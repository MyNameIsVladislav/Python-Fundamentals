from time import time


class Timer:
    def __init__(self, fun):
        self.function = fun

    def __call__(self, *args, **kwargs):
        start = time()
        print(f'Старт: {start}')
        active = self.function(*args, **kwargs)
        end = time()
        print(f'Финиш: {end}\n')
        print(f'Время выполнения функции: {end - start}')
        return f'Последний элемент списка: {active[-1]}'


@Timer
def math_fun(n):
    obj = [sum(range(x)) for x in range(n)]
    return obj


print(math_fun(55000))
