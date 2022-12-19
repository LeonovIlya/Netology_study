nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, list_name):
        self.list_name = list_name
        self.cursor = -1
        self.nest_cursor = 0
        self.list_len = len(self.list_name)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.list_name[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.nest_cursor += 1
        return self.list_name[self.cursor][self.nest_cursor - 1]


print('Итератор.Плоское представление:')
for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print()
print(f'Итератор.Комперхеншн.Плоский список: \n {flat_list}')


def gen_flat_list(list_name):
    for l in list_name:
        for i in l:
            yield i


print()
print('Генератор. Плоское представление.')
for i in gen_flat_list(nested_list):
    print(i)
