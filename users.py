class User():

    def __init__(self, first_name, last_name, sex, age):
        self.fname = first_name
        self.lname = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = 0

    def greet_user(self):
        print(f"Hello, {self.fname.title()}!")

    def describe_user(self):
        print(f"{self.fname.title()} {self.lname.title()}, {self.sex}, {self.age} years old")

    def increment_login_attempts(self):
        self.login_attempts +=1
        print(f"Количество попыток входа: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Счетчик попыток входа сброшен")


class Admin(User):

    def __init__(self, first_name, last_name, sex, age):
        super().__init__(first_name, last_name, sex, age)
        self.privileges = Privileges()





class Privileges():

    def __init__(self):
        self.privileges = ['разрешено удалять пользователей', 'разрешено банить пользователей', 'разрешено добавлять сообщения']

    def show_privileges(self):
        for i in self.privileges:
            print(f"Админу {i}")

            
