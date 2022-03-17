from chapter_9.three import User


class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges()

    def show_privileges(self):
        return f'Admin - {self.privileges}'


class Privileges:
    def __init__(self):
        self.privileges = ['разрешено добавлять сообщения',
                           'разрешено удалять сообщения',
                           'разрешено банить пользователей']

    def show_privileges(self):
        return f'Privileges - {self.privileges}'


if __name__ == '__main__':
    one = Admin(first_name='Ivan',
                last_name='Sidorov',
                email='sidorov.i@email.com')
    print(one.privileges.show_privileges())





