class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f'Имя: {self.first_name}',
              f'Фамилия: {self.last_name}',
              f'Email: {self.email}', sep='\n')

    def greet_user(self):
        print(f'Привет, {self.first_name} {self.last_name}!')


if __name__ == '__main__':
    id_one = User('Dmitry', 'Ivanov', 'd.ivanov@net.com')
    id_two = User('Maria', 'Petrova', 'm.petrova2000@net.com')
    id_three = User('Nadya', 'Sidorova', 'ns@net.com')

    id_one.describe_user()
    id_two.describe_user()
    id_three.describe_user()

    id_one.greet_user()
    id_two.greet_user()
    id_three.greet_user()
