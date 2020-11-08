# Создать класс точки, реализовать конструктор который
# инициализирует 3 координаты (x, y, z). Реалзиовать методы для
# получения и изменения каждой из координат. Перегрузить для этого
# класса методы сложения, вычитания, деления умножения.
# Перегрузить один любой унарный метод.


class Dot:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = value

    def get_y(self):
        return self.y

    def set_y(self, value):
        self.y = value

    def get_z(self):
        return self.z

    def set_z(self, value):
        self.z = value

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Dot(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Dot(x, y, z)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Dot(x, y, z)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z
        return Dot(x, y, z)


dot_1 = Dot(0, 0, 0)
print(f'Точка 1: {dot_1}')

dot_1.set_x(2)
dot_1.set_y(6)
dot_1.set_z(10)
print(f'Set & Get\nТочка 1:'
      '{dot_1.get_x()}, {dot_1.get_y()}, {dot_1.get_z()}\n')

dot_2 = Dot(1, 3, 2)
print(f'Точка 2: {dot_2}\n')

print(f'Перегрузка + | {dot_1 + dot_2}')
print(f'Перегрузка - | {dot_1 - dot_2}')
print(f'Перегрузка * | {dot_1 * dot_2}')
print(f'Перегрузка / | {dot_1 / dot_2}\n')

dot_1 += dot_2
print(f'Унарный + | Точка 1: {dot_1}')
dot_1 -= dot_2
print(f'Унарный - | Точка 1: {dot_1}')
