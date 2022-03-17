from chapter_9.three import User


class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = ['разрешено добавлять сообщения',
                           'разрешено удалять сообщения',
                           'разрешено банить пользователей']

    def show_privileges(self):
        return f'Admin - {self.privileges}'


if __name__ == '__main__':
    one = Admin(first_name='Ivan',
                last_name='Sidorov',
                email='sidorov.i@email.com')
    print(one.show_privileges())
