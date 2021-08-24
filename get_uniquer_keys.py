from collections import Counter


class CoolBookIter:
    counter = 0

    def __init__(self, obj):
        self.simple_dict = obj
        self.sort_dict = Counter()
        self.get_item()

    def get_item(self):
        if self.simple_dict.get("Cook Book"):
            for item in self.simple_dict["Cook Book"]:
                self.get_value(item.popitem())

    def get_value(self, tuple_obj):
        self.sort_dict.update(tuple_obj[1])

    def __get__(self):
        return self.sort_dict

    def __next__(self):
        if self.counter < len(self.sort_dict):
            self.counter += 1
            return list(self.sort_dict.keys())[self.counter-1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __str__(self):
        if self.sort_dict.keys():
            return f"{sorted(self.sort_dict, key=self.sort_dict.get, reverse=True)}"
        else:
            return 'Cook Book - пуста, как и наша жизнь ...' \
                   '\nПопробуй Ещё...'


db = {"Cook Book":
    [
    {"Dish A": ["oil", "bacon", "oil"]},
    {"Dish B": ["eggs", "oil", "eggs"]}
    ]
}
cook_book = CoolBookIter(db)
print(cook_book)
