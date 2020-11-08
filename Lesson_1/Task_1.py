# 1)Создать список из N элементов (от 0 до n с шагом 1).
# В этом списке вывести все четные значения.

N = None

while True:
    input_ = input('Введите размер списка: ')

    if not input_.isdigit():
        print('Ошибка! Размер списка должен быть числом больше/равным 0.')
    else:
        N = int(input_)
        number_list = list(range(0, N))

        for num in number_list:
            if num % 2 == 0:
                print(num)
        break
