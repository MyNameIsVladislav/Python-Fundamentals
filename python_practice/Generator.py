def gen(obj):
    for item in obj[::-1]:
        yield len(item)


list_ = ['one', 'two', 'three', 'long number']
a = gen(list_)
for i in range(1, len(list_) + 1):
    if i == len(list_):
        print(next(a))
    else:
        print(next(a), end=', ')
