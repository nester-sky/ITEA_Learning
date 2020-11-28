# 2) Создать свою структуру данных Словарь, которая поддерживает методы,
# get, items, keys, values. Так же перегрузить операцию сложения для
# словарей, которая возвращает новый расширенный объект.


class MyDict:

    def __init__(self, *args, **kwargs):
        if not args:
            self._dict = dict(kwargs)
        else:
            self._dict = dict(args)

    def __str__(self):
        return str(self._dict)

    def __add__(self, other):
        args = [(k, self._dict[k]) for k in self._dict] +\
               [(k, other._dict[k]) for k in other._dict]
        return MyDict(*args)

    def get(self, key, default=None):
        # for k in self._dict:
        #     if k == key:
        #         return self._dict[k]
        # return default

        try:
            value = self._dict[key]
        except KeyError:
            value = default
        return value

    def items(self):
        # return [(k, v) for k, v in enumerate(self._dict)]
        return [(k, self._dict[k]) for k in self._dict]

    def keys(self):
        return [k for k in self._dict]

    def values(self):
        return [self._dict[k] for k in self._dict]


dict_1 = MyDict(a=0)
dict_2 = MyDict(b=11, c=22, d='33', e='44', f='55')
print('dict_1 \t', dict_1)
print('dict_2 \t', dict_2)

dict_ = dict_1 + dict_2
print('Sum \t', dict_, '\n')

print('Get  w \t\t', dict_.get('w'))
print('Get  w | -1\t', dict_.get('w', -1))
print('Get  b | -1\t', dict_.get('b', -1))

print('Items \t', dict_.items())

print('Keys \t', dict_.keys())

print('Values \t', dict_.values())
