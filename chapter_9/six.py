from chapter_9.one import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(f'Список мороженого {self.flavors}')


if __name__ == '__main__':
    one = IceCreamStand('Макдоналдс', 'Европейская',
                        ['клубничное', 'шоколадное'])
    one.show_flavors()
