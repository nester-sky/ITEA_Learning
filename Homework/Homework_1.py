# Создать классы структур данных:
# 1) Стек
# 2) Очередь.
# Создать класс комплексного числа и реализовать для него
# арифметические операции (не использовать стандартный тип
# complex).


class MyStack:

    def __init__(self):
        self._items = []

    def __str__(self):
        return str(self._items)

    def size(self):
        return len(self._items)

    def empty(self):
        self._items = []

    def put(self, value):
        self._items.append(value)
        print(f'Put value: {value}')

    def get(self):
        if self.size():
            _value = self._items.pop()
            print(f'Get value: {_value}')


class MyQueue(MyStack):

    def put(self, value):
        self._items.insert(0, value)
        print(f'Put value: {value}')


class MyComplex:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'({self._x}, {self._y}i)'

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        return MyComplex(x, y)

    def __sub__(self, other):
        x = self._x - other._x
        y = self._y - other._y
        return MyComplex(x, y)

    def __mul__(self, other):
        x = self._x*other._x - self._y*other._y
        y = self._x*other._y + self._y*other._x
        return MyComplex(x, y)

    def __truediv__(self, other):
        denominator = other._x*other._x + other._y*other._y
        x = (self._x*other._x + self._y*other._y)/denominator
        y = (self._y*other._x - self._x*other._y)/denominator
        return MyComplex(x, y)


print('\n---- Stack ----')
stack = MyStack()

stack.put('s_a')
stack.put('s_b')
stack.put('s_c')

print(f'\nStack: {stack}\n')

stack.get()
stack.get()
stack.get()

print(f'\nStack: {stack}\n')

stack.put('test_item')
print(f'Stack: {stack}')
stack.empty()
print('Emptying example')
print(f'Stack: {stack}')


print('\n---- Queue ----')
queue = MyQueue()

queue.put('q_a')
queue.put('q_b')
queue.put('q_c')

print(f'\nQueue: {queue}\n')

queue.get()
queue.get()
queue.get()

print(f'\nQueue: {queue}\n')


print('\n---- Complex ----')
z1 = MyComplex(4, 6)
z2 = MyComplex(1, 2)

print(f'z1 = {z1}')
print(f'z2 = {z2}\n')

print(f'Операция + | {z1 + z2}')
print(f'Операция - | {z1 - z2}')
print(f'Операция * | {z1 * z2}')
print(f'Операция / | {z1 / z2}\n')
