# 3)Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить
# слово Fizz, а вместо чисел, кратных пяти — слово Buzz. Если число
# кратно пятнадцати, то программа должна выводить слово FizzBuzz.

list_numbers = list(range(0, 100))

for num in list_numbers:
    if num % 15 == 0:
        print('FizzBuzz')
        continue
    if num % 3 == 0:
        print('Fizz')
        continue
    if num % 5 == 0:
        print('Buzz')
        continue
    print(num)