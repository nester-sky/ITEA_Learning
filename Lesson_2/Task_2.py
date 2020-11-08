# Создать класс магазина. Конструктор должен инициализировать
# значения: «Название магазина» и «Количество проданных
# товаров». Реализовать методы объекта, которые будут увеличивать
# кол-во проданных товаров, и реализовать вывод значения
# переменной класса, которая будет хранить общее количество
# товаров проданных всеми магазинами.


class ChainStores:
    total_count = 0
    total_sales = 0

    def __init__(self, name):
        self.chain_name = name

    def get_report(self):
        print(f'| Отчет по продажам сети "{self.chain_name}"')
        print(f'| Кол-во: {self.total_count}')
        print(f'| Сумма: {self.total_sales}\n')


class Shop(ChainStores):
    shop_count = 0
    shop_sales = 0

    def __init__(self, name, count, sales):
        self.shop_name = name
        self.shop_count = count
        self.shop_sales = sales

        ChainStores.total_count += count
        ChainStores.total_sales += sales

    def get_report(self):
        print(f'| Отчет по продажам магазина {self.shop_name}')
        print(f'| Кол-во: {self.shop_count}')
        print(f'| Сумма: {self.shop_sales}\n')

    def set_transaction(self, count, cost):
        print(f'[{self.shop_name}]: Транзакция успешна')
        self.shop_count += count
        self.shop_sales += cost
        ChainStores.total_count += count
        ChainStores.total_sales += cost


line = '-'*40 + '\n'

print(line)

my_chain = ChainStores('Sky')
my_chain.get_report()

print(line)
my_shop_1 = Shop('ТТ_1', 10, 2200)
my_shop_1.get_report()

my_shop_2 = Shop('ТТ_2', 30, 9000)
my_shop_2.get_report()

my_shop_3 = Shop('ТТ_3', 23, 32300)
my_shop_3.get_report()
print(line)

my_chain.get_report()

my_shop_1.set_transaction(12, 6000)
my_shop_2.set_transaction(5, 500)
print('\n', line)

my_chain.get_report()
