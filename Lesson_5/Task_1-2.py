# 1) Создать декоратор, который будет запускать функцию в отдельном
# потоке. Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.

# 2) Создать функцию, которая будет скачивать файл из интернета по
# ссылке, повесить на неё декоратор, который будет запускать целевую
# функцию каждый раз в отдельном потоке. Создать список из 10
# ссылок, по которым будет происходить скачивание. Каждый поток
# должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание
# закончится.

import urllib.request
from time import sleep
from threading import Thread, active_count
from functools import wraps


class DecoratorThread:

    def __init__(self, thread_name, is_daemon=False):
        self._thread_name = thread_name
        self._is_daemon = is_daemon

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            th_name = self._thread_name + '_' + str(active_count())
            thread = Thread(target=func, args=(*args,), kwargs={**kwargs},
                            name=th_name, daemon=self._is_daemon)
            thread.start()

        return decorated


@DecoratorThread(thread_name='MyThread', is_daemon=False)
def download_file(url):
    print(f'Начало скачивания файла. \tСсылка: {url}')
    file_name = url.split("/")[-1]
    urllib.request.urlretrieve(url, file_name)
    print(f'Файл успешно скачан. \t\tСсылка: {url}')


links = [
    'https://coursehunter.net/uploads/categories/python.png',
    'https://radiokp.ru/sites/default/files/2020-05/1_357.jpg',
    'https://cdnimg.rg.ru/img/content/178/22/40/kotik_d_850.jpg',
    'https://sharij.net/wp-content/uploads/2017/05/kot.jpg',
    'https://peterburg2.ru/uploads/20/03/04/ga11_hu65f.JPG',
    'https://i.ytimg.com/vi/1Ne1hqOXKKI/maxresdefault.jpg',
    'https://i.ytimg.com/vi/2giQVPIl9JM/maxresdefault.jpg',
    'https://i.ytimg.com/vi/mK72EwuxZAU/hqdefault.jpg',
    'https://i.work.ua/article/2385b.jpg',
    'https://i.work.ua/img/00003927_s.jpg',
]

result = list(map(download_file, links))
