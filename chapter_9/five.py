class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f'Имя: {self.first_name}',
              f'Фамилия: {self.last_name}',
              f'Email: {self.email}', sep='\n')

    def greet_user(self):
        print(f'Привет, {self.first_name} {self.last_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == '__main__':
    dmitry = User('Dmitry', 'Ivanov', 'ivanov.d@email.com')
    for _ in range(5):
        dmitry.increment_login_attempts()
    print(dmitry.login_attempts)
    dmitry.reset_login_attempts()
    print(dmitry.login_attempts)
