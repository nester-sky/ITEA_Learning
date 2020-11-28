# 1) Создать свою структуру данных Список, которая поддерживает
# индексацию. Методы pop, append, insert, remove, clear. Перегрузить
# операцию сложения для списков, которая возвращает новый расширенный
# объект.


class MyList:

    def __init__(self, *args):
        self._list = [n for n in args]

    def __str__(self):
        return str(self._list)

    def __add__(self, other):
        args = tuple(self._list + other._list)
        return MyList(*args)

    def pop(self, index=None):
        if index is None:
            del self._list[-1:]
        else:
            del self._list[index]

    def append(self, value):
        self._list[len(self._list):] = [value]

    def insert(self, index, value):
        start = self._list[:index]
        end = self._list[index:]
        self._list = start + [value] + end

    def remove(self, value):
        # for i, v in enumerate(self._list):
        #     if v == value:
        #         del self._list[i]
        #         return v

        counter = 0
        for v in self._list:
            if v == value:
                del self._list[counter]
                return v
            else:
                counter += 1

        raise ValueError(f'{value} - отсутствует в списке')

    def clear(self):
        del self._list[:]


list_1 = MyList(0)
list_2 = MyList(11, 22, '33', '44', '55')
print('list_1 \t', list_1)
print('list_2 \t', list_2)

list_ = list_1 + list_2
print('Sum \t', list_, '\n')

list_.pop()
list_.pop(1)
print('Pop x2\t', list_)

list_.append('55')
print('Append \t', list_)

list_.insert(1, 11)
print('Insert \t', list_)

list_.remove(0)
print('Remove \t', list_)

list_.remove(0)
