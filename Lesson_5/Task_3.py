# 3) Написать свой контекстный менеджер для работы с файлами.


class Open:

    file = None

    def __init__(self, file_name, mode):
        self._file_name = file_name
        self._mode = mode

    def __enter__(self):
        self.file = open(self._file_name, self._mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with Open('test.txt', 'w') as file:
    file.write('TEST ROW')
