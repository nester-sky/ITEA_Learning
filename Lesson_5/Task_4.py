# 4) Дополнение к предыдущей работе с соц. Сетью. Все хранение
# данных пользователей реализовать на основе модуля shelve.

import shelve
import re
from os import system
from datetime import datetime
from functools import wraps

DATE_FORMAT = "%d.%m.%Y %H:%M:%S"
FILE = 'SOCIAL_NETWORK'


# фун-ция для корректного выбора пунктов меню
def input_(msg):
    while True:
        try:
            result = int(input(msg))
            return result
        except ValueError:
            pass


class OpenShelve:

    def __init__(self, filename):
        self._filename = filename

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):

            with shelve.open(self._filename) as db:
                kwargs['db'] = db
                return func(*args, **kwargs)

        return decorated


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
    # авторизованный пользователь
    _current_user = {}

    @OpenShelve(FILE)
    def set_logins(self, login, db=None):
        temp = db['list_all_logins']
        temp.append(login)
        db['list_all_logins'] = temp

    @OpenShelve(FILE)
    def get_logins(self, db=None):
        return db['list_all_logins']

    @OpenShelve(FILE)
    def set_users(self, user, db=None):
        temp = db['list_all_users']
        temp.append(user)
        db['list_all_users'] = temp

    @OpenShelve(FILE)
    def get_users(self, db=None):
        return db['list_all_users']

    def set_default_db(self, db=None):
        db['list_all_logins'] = ['admin']
        db['list_all_users'] = [Authorization._SUPER_ADMIN]
        db['list_all_posts'] = []

    @OpenShelve(FILE)
    def check_shelve(self, db=None):
        if len(db) == 0:
            self.set_default_db(db)

    def set_current_user(self, user):
        Authorization._current_user = user

    def get_current_user(self):
        return Authorization._current_user

    def get_user_param(self, param):
        return Authorization._current_user[param]

    def registration(self, login, password, name):

        self.set_logins(login)
        id_ = len(self.get_logins()) + 1
        dt_reg = datetime.now().strftime(DATE_FORMAT)

        new_user = {
            'id': id_,
            'dt_registration': dt_reg,
            'name': name,
            'login': login,
            'password': password,
            'flag_admin': False,
        }
        self.set_users(new_user)

        msg = 'Поздравляю! Вы зарегистрированы в ПСС :)'
        return msg

    def authentication(self, login, password):
        flag, self_ = False, None
        msg = 'Не правильный логин или пароль'

        for user in self.get_users():
            if (user['login'] == login) & (user['password'] == password):
                msg = 'Авторизация в ПСС прошла успешно'
                # запоминаем текущего, авторизированого пользователя
                self.set_current_user(user)
                flag = True
                self_ = self
                break
        return flag, msg, self_

    def check_login(self, login):
        flag, msg = False, ''
        all_logins = set(self.get_logins())

        if len(login) < 3:
            msg = 'Логин должен быть больше 3-х символов'
        elif login not in all_logins:
            flag = True
        else:
            msg = 'Такой логин уже существует'

        return flag, msg

    def check_password(self, password):
        flag, msg = False, ''

        # регулярка для шаблона пароля (описание внизу функции)
        regular = r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$'
        pattern = re.compile(regular)

        flag = bool(pattern.match(password))
        if not flag:
            msg = 'Требования к паролю:\n'\
                  '- хотя бы одно число (0-9)\n'\
                  '- хотя бы одна прописная буква (A-Z)\n'\
                  '- хотя бы одна строчная буква (a-z)\n'\
                  '- не менее 8 символов\n'
        return flag, msg


class Posts:

    @OpenShelve(FILE)
    def set_posts(self, post, db=None):
        temp = db['list_all_posts']
        temp.append(post)
        db['list_all_posts'] = temp
        return None

    @OpenShelve(FILE)
    def get_posts(self, db=None):
        return db['list_all_posts']

    def all_post(self, flag_admin, user_login):
        list_posts = []
        for post in self.get_posts():
            post_msg = '_____________________________________________\n\n'\
                       f" Код статьи: {post['id']}\n"\
                       f" Пользователь: {post['user']}\n"\
                       f" Дата публикации: {post['dt_post']}\n"\
                       f" Заглавие статьи: {post['title']}\n"\
                       f" Содержание статьи: {post['body']}\n"\
                       '_____________________________________________'
            if flag_admin:
                list_posts.append(post_msg)
            else:
                if user_login == post['user']:
                    list_posts.append(post_msg)
        return list_posts

    def add_post(self, user, title, body):
        # 1000 - просто для старта кодов статей с 1к
        id_ = len(self.get_posts()) + 1000
        dt_post = datetime.now().strftime(DATE_FORMAT)
        post = {
            'id': id_,
            'dt_post': dt_post,
            'user': user,
            'title': title,
            'body': body,
        }
        self.set_posts(post)
        return f'Пост "{title}" опубликован'


class Users(Authorization, Posts):

    def get_flag_admin(self):
        return self.get_user_param('flag_admin')

    def get_all_users(self):
        list_users = []
        for user in self.get_users():
            user_msg = '_____________________________________________\n\n'\
                       f" Код: {user['id']}\n"\
                       f" Дата регистрации: {user['dt_registration']}\n"\
                       f" Логин: {user['login']}\n"\
                       f" Имя: {user['name']}\n"\
                       '_____________________________________________'
            list_users.append(user_msg)
        return list_users

    def set_post(self, title, body):
        result = self.add_post(self.get_user_param('login'), title, body)
        return result

    def get_all_post(self):
        flag_admin = self.get_user_param('flag_admin')
        user_login = self.get_user_param('login')
        result = self.all_post(flag_admin, user_login)
        return result


def set_registration_data():
    flag, msg = False, ''
    while not flag:
        login = input(f'Введите логин: ')
        flag, msg = Authorization().check_login(login)
        print(msg)

    flag, msg = False, ''
    while not flag:
        password = input(f'Введите пароль: ')
        flag, msg = Authorization().check_password(password)
        if flag:
            flag = False
            password_2 = input('Введите пароль ещё раз: ')
            if password == password_2:
                flag = True
            else:
                msg = 'Пароли не совпадают'
        print(msg)

    name = input('Введите Ваше имя: ')
    return login, password, name


system('cls')
Authorization().check_shelve()
line = '_____________________________________________\n'
print(line)
print('   Приветствую в "Подобие Социальной Сети"   ')
print(line)

# вечный цикл для смены дейстий пользователей
while True:
    # флаг выхода из программы
    close = False
    print(line)
    print('1 - Авторизоваться в ПСС')
    print('2 - Зарегистрироваться в ПСС \n')
    print('0 - Выход из программы \n')
    choice = input_('Сделайте Ваш выбор: ')

    if choice == 1:
        # цикл для попыток авторизации
        while choice == 1:
            print(line)
            # запрашиваем и проверяем логин, пароль пользователя
            login = input(f'Введите логин: ')
            password = input(f'Введите пароль: ')
            flag, msg, session = Users().authentication(login, password)
            # если авторизация произошла с ошибкой (логина/пароля)
            if not flag:
                system('cls')
                print(line)
                # текст ошибки
                print(msg)
                print(line)
                print('1 - Попробовать снова')
                print('2 - Зарегистрироваться в ПСС\n')
                print('0 - Выход из программы \n')
                choice = input_('Сделайте Ваш выбор: ')

                if choice == 2:
                    login, password, name = set_registration_data()
                    session = Users().registration(login, password, name)
                    choice = -1
            # если авторизация прошла успешно
            else:
                is_admin = session.get_flag_admin()

                # цикл меню дейстий пользователя
                while choice not in (0, 9):
                    print(line)
                    print('1 - Посмотреть все посты в ПСС')
                    print('2 - Создать новый пост в ПСС\n')
                    if is_admin:
                        print('3 - Вывод всех пользователей ПСС\n')
                    print('9 - Выйти из учетной записи')
                    print('0 - Выход из программы \n')
                    choice = input_('Сделайте Ваш выбор: ')
                    system('cls')

                    if choice == 1:
                        print(line)
                        result = session.get_all_post()
                        for val in result:
                            print(val)
                        choice = -1

                    elif choice == 2:
                        print(line)
                        title = input('Введите название статьи: ')
                        body = input('Введите содержание статьи: ')
                        result = session.set_post(title, body)
                        print(result)
                        choice = -1

                    elif is_admin & (choice == 3):
                        result = session.get_all_users()
                        for val in result:
                            print(val)

                    elif choice == 9:
                        del session

    elif choice == 2:
        print(line)
        login, password, name = set_registration_data()
        Users().registration(login, password, name)

    if choice == 0:
        close = True

    if close:
        print(line)
        print('   До встречи в "Подобие Социальной Сети"    ')
        print(line)
        break

print('\n\n\n')
