
def gen(obj):
    for item in obj[::-1]:
        yield len(item)


list_obj = ['one', 'two', 'three', 'long number']
iter_obj = gen(list_obj)
for element in range(1, len(list_obj) + 1):
    if element == len(list_obj):
        print(next(iter_obj))
    else:
        print(next(iter_obj), end=', ')
