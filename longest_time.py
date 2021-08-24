"""
Напишите функцию, которая будет принимать три значения: h (часы), m (минуты), s (секунды).
Функция должна возвращать значение, соответствующее самому длительному периоду времени.

Примечание: среди передаваемых временных промежутков не будет одинаковых.

"""


def max_time(time_input):
    seconds, res = 0, 0
    if len(time_input) == 3:
        for degree, item in enumerate(time_input[::-1]):
            degree = 60 ** degree
            if seconds < item * degree:
                seconds = item * degree
                res = item
        return res


try:
    obj_time = list(map(int, input('Введите h (часы), m (минуты), s (секунды): ').split(',')))
    print(max_time(obj_time))
except ValueError:
    print("Несоответствующее значение")
