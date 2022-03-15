class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):

        print(f'Название ресторана: {self.name}')
        print(f'Кухня: {self.cuisine}')

    def open_restaurant(self):

        print('Ресторан открыт!')


if __name__ == '__main__':
    restaurant = Restaurant('Макдоналдс', 'Европейская')
    print(restaurant.name)
    print(restaurant.cuisine)

    restaurant.describe_restaurant()
    restaurant.open_restaurant()
