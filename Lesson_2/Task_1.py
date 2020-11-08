# Создать класс автомобиля. Создать классы легкового автомобиля
# и грузового. Описать в основном классе базовые атрибуты и методы
# для автомобилей. Будет плюсом если в классах наследниках
# переопределите методы базового класса.


class Cars:
    current_transmission = 0

    def __init__(self, make, year, color):
        self.make = make
        self.year = year
        self.color = color

    def set_signaling(self, flag):
        if flag:
            print('Автомобиль поставлен на сигнализацию')
        else:
            print('Автомобиль снят с сигнализации')

    def set_transmission(self, transmission):
        self.current_transmission = transmission
        print(f'Установлена передача: {transmission}')

    def run(self):
        if self.current_transmission >= 1:
            print('Автомобиль поехал вперёд')
        elif self.current_transmission == -1:
            print('Автомобиль поехал назад')
        else:
            print('Перед движением переключите передачу')

    def stop(self):
        self.set_transmission(0)
        print('Автомобиль остановился')


class PassengerCar(Cars):

    def set_signaling(self, flag):
        if flag:
            print(f'Легковой автомобиль {self.make},'
                  'цвет {self.color} поставлен на сигнализацию')
        else:
            print(f'Легковой автомобиль {self.make},'
                  'цвет {self.color} снят с сигнализации')

    def set_transmission(self, transmission):
        if transmission == 'N':
            self.current_transmission = -2
        elif transmission == 'R':
            self.current_transmission = -1
        elif transmission == 'P':
            self.current_transmission = 0
        elif transmission == 'D':
            self.current_transmission = 1

        print(f'Установлена передача: {transmission}')

    def stop(self):
        self.set_transmission('P')
        print('Автомобиль остановился')


class FreightCar(Cars):

    def set_signaling(self, flag):
        if flag:
            print(f'Грузовик {self.make},'
                  'цвет {self.color} поставлен на сигнализацию')
        else:
            print(f'Грузовик {self.make},'
                  'цвет {self.color} снят с сигнализации')

    def set_transmission(self, transmission, type_=''):
        if type_ == 'H':
            type_ = 'повышенная '
        elif type_ == 'L':
            type_ = 'пониженная '

        self.current_transmission = transmission

        print(f'Установлена {type_}передача: {transmission}')


none_car = Cars(None, None, None)

none_car.set_signaling(False)
none_car.run()
none_car.set_transmission(1)
none_car.run()
none_car.stop()
none_car.set_signaling(True)
print()


passenger_car = PassengerCar('Nissan', 2017, 'Белый')

passenger_car.set_signaling(False)
passenger_car.run()
passenger_car.set_transmission('R')
passenger_car.run()
passenger_car.stop()
passenger_car.set_signaling(True)
print()


freight_car = FreightCar('Volvo', 2015, 'Черный')

freight_car.set_signaling(False)
freight_car.run()
freight_car.set_transmission(1, 'L')
freight_car.run()
freight_car.stop()
freight_car.set_signaling(True)
print()
