# Создать подобие социальной сети.

# 1) Создать класс авторизации, в котором описать методы
# регистрации, аутентификации, добавить методы
# проверки на валидность пароля (содержание символов и цифр),
# проверка на уникальность логина пользователя.
# В классовых переменных хранить всех пользователей сети.
# (Отдельно объекты этого класса создаваться не будут,
# такие классы называются миксинами)

# 2) Создать класс пользователя, наследующий класс авторизации,
# который будет разделять роли админа и простого пользователя
# (этот вопрос можно решить с помощью флага is_admin,
# либо создав 2 разных класса для админа
# и обычного пользователя и наследовать их).
# На момент создания каждого объекта этого класса,
# в переменную объекта сохранять время и дату его создания.

# 3) Создать класс поста, который имеет дату публикации и её содержимое.

# Что должно быть в клиентском коде:
# Человек заходит, и имеет возможность зарегистрироваться
# (ввод логин, пароль, подтверждение пароля),
# далее входит в свою учетную запись.
# Добавить возможность выхода из учетной записи, и вход в новый аккаунт.
# При входе под обычным пользователем мы можем создать новый пост,
# с определённым содержимым.
# Под учётной записью администратора мы можем
# увидеть всех пользователей нашей системы,
# дату их регистрации, и их посты.

import re
from os import system
from datetime import datetime

DATE_FORMAT = "%d.%m.%Y %H:%M:%S"


# фун-ция для корректного выбора пунктов меню
def input_(msg):
    while True:
        try:
            result = int(input(msg))
            return result
        except ValueError:
            pass


class Authorization:
    # Статическая учётка Администратора
    _SUPER_ADMIN = {
        'id': 0,
        'dt_registration': '00.00.0000',
        'name': 'Administrator',
        'login': 'admin',
        'password': 'admin',
        'flag_admin': True,
    }

    # храним отдельный список логинов, для быстрого поиска
    _list_all_logins = ['admin']
    _list_all_users = [_SUPER_ADMIN]
    # авторизованный пользователь
    current_user = {}

    def registration(self):
        login = self.check_login()
        password = self.check_password()
        name = input('| Введите Ваше имя: ')

        self._list_all_logins.append(login)
        id_ = len(self._list_all_logins) + 1
        dt_reg = datetime.now().strftime(DATE_FORMAT)

        new_user = {
            'id': id_,
            'dt_registration': dt_reg,
            'name': name,
            'login': login,
            'password': password,
            'flag_admin': False,
        }
        self._list_all_users.append(new_user)

        system('cls')
        print(' _____________________________________________ ')
        print('|                                             |')
        print('|   Поздравляю! Вы зарегистрированы в ПСС :)  |')
        print('|_____________________________________________|')

    def authentication(self):
        login = input('| Введите логин: ')
        # трансформация списка в множество для быстрого поиска
        all_logins = set(self._list_all_logins)
        if login not in all_logins:
            msg = '| Такой пользователь не загеристрирован\n|'
            return False, msg
        else:
            password = input('| Введите пароль: ')
            for user in self._list_all_users:
                if (user['login'] == login) & (user['password'] == password):
                    system('cls')
                    print(' _____________________________________________ ')
                    print('|                                             |')
                    print('|   Авторизация в ПСС прошла успешно          |')
                    print('|_____________________________________________|\n|')
                    # запоминаем текущего, авторизированого пользователя
                    self.current_user = user
                    return True, self
            msg = '| Не правильный логин или пароль\n|'
            return False, msg

    def check_login(self):
        login = input('| Введите логин: ')

        all_logins = set(self._list_all_logins)

        while True:
            if len(login) < 3:
                msg = 'Логин должен быть больше 3-х символов\n|\n'
            elif login not in all_logins:
                return login
            else:
                msg = 'Такой логин уже существует\n|\n'

            login = input(f'| {msg}| Введите новый логин: ')

    def check_password(self):
        # регулярка для шаблона пароля (описание внизу функции)
        regular = r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$'
        pattern = re.compile(regular)

        password = input('| Введите пароль: ')
        while True:
            result = bool(pattern.match(password))
            # result = True # Отключает проверку шаблона пароля
            if result:
                password_2 = input(f'| Введите пароль ещё раз: ')
                if password == password_2:
                    return password
                else:
                    msg = ' ____________________________________________\n|\n'\
                          '| Пароли не совпадают\n|\n'
            else:
                msg = ' _____________________________________________\n|\n'\
                      '| Требования к паролю:\n'\
                      '| - хотя бы одно число (0-9)\n'\
                      '| - хотя бы одна прописная буква (A-Z)\n'\
                      '| - хотя бы одна строчная буква (a-z)\n'\
                      '| - не менее 8 символов\n'\
                      '|_____________________________________________\n|\n'

            system('cls')
            password = input(f'{msg}| Введите новый пароль: ')


class Posts:
    _all_posts = []

    def all_post(self, user):
        system('cls')
        for post in self._all_posts:
            post_msg = '_____________________________________________\n'\
                        f" Код статьи: {post['id']}\n"\
                        f" Пользователь: {post['user']}\n"\
                        f" Дата публикации: {post['dt_post']}\n"\
                        f" Заглавие статьи: {post['title']}\n"\
                        f" Содержание статьи: {post['body']}\n"\
                        '_____________________________________________'
            if user['flag_admin']:
                print(post_msg)
            else:
                if user['login'] == post['user']:
                    print(post_msg)

    def add_post(self, user, title, body):
        # 1000 - просто для старта кодов статей с 1к
        id_ = len(self._all_posts) + 1000
        dt_post = datetime.now().strftime(DATE_FORMAT)
        post = {
            'id': id_,
            'dt_post': dt_post,
            'user': user,
            'title': title,
            'body': body,
        }
        self._all_posts.append(post)
        return f'|\n| Пост "{title}" опубликован'


class Users(Authorization, Posts):

    def get_flag_admin(self):
        return self.current_user['flag_admin']

    def get_all_users(self):
        for user in self._list_all_users:
            user_msg = '_____________________________________________\n'\
                       f" Код: {user['id']}\n"\
                       f" Дата регистрации: {user['dt_registration']}\n"\
                       f" Логин: {user['login']}\n"\
                       f" Имя: {user['name']}\n"\
                       '_____________________________________________'
            print(user_msg)

    def set_post(self):
        title = input('| Введите название статьи: ')
        body = input('| Введите содержание статьи: ')
        result = self.add_post(self.current_user['login'], title, body)
        return result

    def get_all_post(self):
        self.all_post(self.current_user)


system('cls')
line = '\\_____________________________________________\n|'
print(' _____________________________________________ ')
print('|                                             |')
print('|   Приветствую в "Подобие Социальной Сети"   |')
print('|_____________________________________________|\n|')

# вечный цикл для смены дейстий пользователей
while True:
    # флаг выхода из программы
    close = False
    print(line)
    print('| 1 - Авторизоваться в ПСС')
    print('| 2 - Зарегистрироваться в ПСС \n|')
    print('| 0 - Выход из программы \n|')
    choice = input_('| Сделайте Ваш выбор: ')

    if choice == 1:
        # цикл для попыток авторизации
        while choice == 1:
            print(line)
            # запрашиваем и проверяем логин, пароль пользователя
            flag, session = Users().authentication()
            # если авторизация произошла с ошибкой (логина/пароля)
            if not flag:
                system('cls')
                print(line)
                # текст ошибки
                print(session)
                print('| 1 - Попробовать снова')
                print('| 2 - Зарегистрироваться в ПСС\n|')
                print('| 0 - Выход из программы \n|')
                choice = input_('| Сделайте Ваш выбор: ')

                if choice == 2:
                    print(line)
                    session = Users().registration()
                    choice = -1
            # если авторизация прошла успешно
            else:
                is_admin = session.get_flag_admin()

                # цикл меню дейстий пользователя
                while choice not in (0, 9):
                    print(line)
                    print('| 1 - Посмотреть все посты в ПСС')
                    print('| 2 - Создать новый пост в ПСС\n|')
                    if is_admin:
                        print('| 3 - Вывод всех пользователей ПСС\n|')
                    print('| 9 - Выйти из учетной записи')
                    print('| 0 - Выход из программы \n|')
                    choice = input_('| Сделайте Ваш выбор: ')
                    system('cls')

                    if choice == 1:
                        print(line)
                        session.get_all_post()
                        choice = -1

                    elif choice == 2:
                        print(line)
                        result = session.set_post()
                        print(result)
                        choice = -1

                    elif is_admin & (choice == 3):
                        session.get_all_users()

                    elif choice == 9:
                        del session

    elif choice == 2:
        print(line)
        Users().registration()

    if choice == 0:
        close = True

    if close:
        print('|_____________________________________________ ')
        print('|                                             |')
        print('|   До встречи в "Подобие Социальной Сети"    |')
        print('|_____________________________________________|')
        break

print('\n\n\n')
