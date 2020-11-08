# Создать декоратор, который принимает на вход аргумент «количество
# повторений». Который будет вызывать функцию, определенное кол-во
# раз. Декорируемая функция должна возвращать:
# 1) Количество времени затраченное на каждый вызов;
# 2) Количество времени затраченное в общей сложности на все вызовы;
# 3) Имя декорируемой функции;
# 4) Значение последнего результата выполнения.

from time import time, sleep
from random import random
from functools import wraps


def lead_time(number_of_cycles=1):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            decorator_report = {
                'function_name': None,
                'total_time': None,
                'cycles_time': None,
                'last_result': None,
            }
            list_calling_loops = {}

            total_time_start = time()
            for i in range(1, number_of_cycles + 1):
                tm_s = time()
                result_func = func(*args, **kwargs)
                result_time = str(round(time() - tm_s, 3))
                list_calling_loops.update({i: result_time})
            total_time_result = str(round(time() - total_time_start, 3))

            decorator_report['function_name'] = func.__name__
            decorator_report['total_time'] = total_time_result
            decorator_report['cycles_time'] = list_calling_loops
            decorator_report['last_result'] = result_func

            return decorator_report

        return wrapper

    return decorator


@lead_time(number_of_cycles=3)
def sleep_function(coefficient=1):
    tm_sleep = round(random()*coefficient, 3)
    sleep(tm_sleep)
    return 'Sleep: ' + str(tm_sleep)


decorator_result = sleep_function()

print(f"Имя декорируемой функции: {decorator_result['function_name']}")
print(f"Последний результат выполнения: {decorator_result['last_result']}")
print(f"Время затраченное на все вызовы: {decorator_result['total_time']} сек")
print('Время затраченное на каждый вызов:')
for k, v in decorator_result['cycles_time'].items():
    print(f'\tВызов №{str(k)}. Время: {v} сек')
