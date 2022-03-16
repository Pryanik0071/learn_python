class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Название ресторана: {self.name}')
        print(f'Кухня: {self.cuisine}')

    def open_restaurant(self):
        print('Ресторан открыт!')

    def set_number_served(self, number):
        """Задать кол-во обслуженных посетителей"""
        self.number_served = number

    def increment_number_served(self, number):
        """Увеличивает кол-во обсулиженных посетителей"""
        self.number_served += number

if __name__ == '__main__':
    restaurant = Restaurant('Макдоналдс', 'Европейская')
    print(restaurant.number_served)
    restaurant.number_served = 15
    restaurant.name = 'Test_Name'
    print(restaurant.name)
    print(restaurant.number_served)
    print(restaurant.describe_restaurant())
    restaurant.set_number_served(30)
    print(restaurant.number_served)
    restaurant.increment_number_served(150)
    print(restaurant.number_served)
