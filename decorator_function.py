from functools import wraps
from time import time


def my_decorator(fun):
    @wraps(fun)
    def timer(n):
        start = time()
        res = fun(n)
        return f'Время работы фукции: {time() - start}\nПоследний элемент: {res[-1]}'
    return timer


@my_decorator
def math_fun(n):
    """ Эту функцию декарируют """

    obj = [sum(range(x)) for x in range(n)]
    return obj


print(math_fun(5500))
print(math_fun.__name__, ' <-', math_fun.__doc__)
