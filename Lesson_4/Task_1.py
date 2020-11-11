# Создайте класс ПЕРСОНА с абстрактным методом, позволяющим вывести
# на экран информацию о персоне, а также реализовать обычный метод
# определения возраста (в текущем году). Создайте дочерние классы:
# АБИТУРИЕНТ (фамилия, дата рождения, факультет),
# СТУДЕНТ (фамилия, дата рождения, факультет, курс),
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# со своими методами возврата информации.
# Создайте список из объектов персон, вывести информацию о
# каждом объекте, а также организуйте поиск персон, чей возраст попадает в
# заданный с клавиатуры диапазон.

from abc import ABC, abstractmethod
from datetime import datetime

DATE_FORMAT = "%d.%m.%Y"


def valid_input(prt):
    while True:
        input_ = input(prt)

        if not input_.isdigit():
            print('Ошибка! Введите число больше 0!')
        else:
            return int(input_)


class Person(ABC):

    def __init__(self, first_name, last_name, birthday):
        self._first_name = first_name
        self._last_name = last_name
        self._birthday = birthday

    @abstractmethod
    def __str__(self):
        pass

    def _age(self):
        birthday = datetime.strptime(self._birthday, DATE_FORMAT)
        age = (datetime.now() - birthday).days // 365
        return age

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value

    @property
    def age(self):
        return self._age()


class Enrollee(Person):

    def __init__(self, first_name, last_name, birthday, faculty):
        super().__init__(first_name, last_name, birthday)
        self._faculty = faculty

    def __str__(self):
        prt = f' ______________________________________\n|' \
              f'\n| Абитуриент: {self._last_name} {self._first_name}' \
              f'\n| Дата рождения: {self._birthday} ({self.age} лет)' \
              f'\n| Факультет: {self._faculty}' \
              f'\n|______________________________________'
        return prt

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self, value):
        self._faculty = value


class Student(Person):

    def __init__(self, first_name, last_name, birthday,
                 faculty, course):
        super().__init__(first_name, last_name, birthday)
        self._faculty = faculty
        self._course = course

    def __str__(self):
        prt = f' ______________________________________\n|' \
              f'\n| Студент: {self._last_name} {self._first_name}' \
              f'\n| Дата рождения: {self._birthday} ({self.age} лет)' \
              f'\n| Факультет: {self._faculty}' \
              f'\n| Курс: {self._course}-й' \
              f'\n|______________________________________'
        return prt

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self, value):
        self._faculty = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value


class Teacher(Person):

    def __init__(self, first_name, last_name, birthday,
                 faculty, position, experience):
        super().__init__(first_name, last_name, birthday)
        self._faculty = faculty
        self._position = position
        self._experience = experience

    def __str__(self):
        prt = f' ______________________________________\n|' \
              f'\n| Преподаватель: {self._last_name} {self._first_name}' \
              f'\n| Дата рождения: {self._birthday} ({self.age} лет)' \
              f'\n| Факультет: {self._faculty}' \
              f'\n| Должность: {self._position}' \
              f'\n| Стаж работы: {self._experience}' \
              f'\n|______________________________________'
        return prt

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self, value):
        self._faculty = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value


people = []

people.append(Enrollee('Иван', 'Иванов', '02.02.2002',
                       'Компьютерных технологий'))

people.append(Student('Петр', 'Петров', '10.10.2000',
                      'Компьютерных технологий', 2))

people.append(Teacher('Федор', 'Федоров', '31.12.1988',
                      'Компьютерных технологий',
                      'Заведующий кафедрой', 7))

print('\t~ Вывод всех личностей ~')
for person in people:
    print(person)

print('\n\nВведите диапазон возраста для поиска:')
from_ = valid_input('От ')
to = valid_input('До ')

print('\n\t  ~ Результат поиска ~')
for person in people:
    if (person.age >= from_) & (person.age <= to):
        print(person)
