'''class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        print(f"{self.name.title()} rolled over")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print(f"My dog's name is {your_dog.name.title()}")
print(f"My dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()

print(f"My dog's name is {my_dog.name.title()}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()
'''

'''
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This is {self.restaurant_name.title()} - restaurant of {self.cuisine_type} cuisine")

    def open_rtstaurant(self):
        print(f"Restaurant {self.restaurant_name.title()} is open")

    def set_served_numbers(self, numbers):
        self.number_served = numbers
        print(f"Now served {self.number_served} persons")

    def increment_served_numbers(self,second_served):
        self.number_served += second_served
        print(f"Total served are {self.number_served}")

res = Restaurant('beryozka', 'russian')
res.describe_restaurant()
res.set_served_numbers(15)
res.increment_served_numbers(14)
'''



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




user = User('ivan', 'ivanov', 'male', 23)

user.greet_user()
user.describe_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
user.increment_login_attempts()










'''
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 25

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles





my_used_car = Car('audi', 'a4', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
'''


