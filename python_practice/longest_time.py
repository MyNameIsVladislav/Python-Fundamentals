"""
Напишите функцию, которая будет принимать три значения: h (часы), m (минуты), s (секунды).
Функция должна возвращать значение, соответствующее самому длительному периоду времени.

Примечание: среди передаваемых временных промежутков не будет одинаковых.

"""


def max_time(time_):
    seconds, res = 0, 0
    if len(time_) == 3:
        for k, i in enumerate(time_[::-1]):
            k = 60 ** k
            if seconds < i * k:
                seconds = i * k
                res = i
        return res


try:
    obj_time = list(map(int, input().split(',')))
    print(max_time(obj_time))
except ValueError:
    print("Несоответствующее значение")