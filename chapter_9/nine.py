"""Task - 9.9. Обновление аккумулятора"""

class Car:
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back ad odometer!')

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f'This car has a {self.battery_size}--kWh battery.')

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range_ = 260
        elif self.battery_size == 100:
            range_ = 315
        else:
            range_ = 'Don\'t know'

        print(f'This car can go about {range_} miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Представляет аспекты машин, специфические для электромобилей"""

    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery_size = Battery()


if __name__ == '__main__':
    tesla = ElectricCar('Tesla', 'New', 2015)
    tesla.battery_size.get_range()
    tesla.battery_size.upgrade_battery()
    tesla.battery_size.get_range()
