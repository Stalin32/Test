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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['малина', 'клубника', 'шоколад']

    def icecream(self):
        print(f"В ресторане подают мороженое со следующими вкусами: {self.flavors}")


res = IceCreamStand('beryozka', 'russian')
res.describe_restaurant()
res.set_served_numbers(15)
res.increment_served_numbers(14)
res.icecream()