class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")


#This code creates a resturant class where i can store resturants's name and cusine type nad it also has two simple functions
# which will describe the resturant and show its open 