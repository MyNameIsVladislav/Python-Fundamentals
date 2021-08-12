
class MyIterator:
    def __init__(self, string):
        self.string = string
        self.len_ = len(string)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.len_:
            self.count += 1
            return self.string[self.count-1]
        else:
            raise StopIteration


s = 'wis_software'
iterator_ = MyIterator(s)

while True:
    print(next(iterator_))