#classes

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment
    
# Creating an instance of the Restaurant class
restaurant = Restaurant("the bear", "Italian")

print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()


# Creating three instances of the Restaurant class
restaurant1 = Restaurant("Gotham Grille", "American")
restaurant2 = Restaurant("Arkham Eats", "Italian")
restaurant3 = Restaurant("Metropolis Cafe", "Greek")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# Printing the initial number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Changing the value of customers served and printing it again
restaurant.number_served = 50
print(f"Updated number of customers served: {restaurant.number_served}")

# Using the set_number_served() method to set a new value
restaurant.set_number_served(100)
print(f"Updated number of customers served after setting: {restaurant.number_served}")

# Incrementing the number of customers served using increment_number_served()
restaurant.increment_number_served(30)
print(f"Number of customers served after incrementing: {restaurant.number_served}")


#child class
class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint']

    def display_flavors(self):
        print("Available Flavors:")
        for flavor in self.flavors:
            print(flavor)

# Creating an instance 
ice_cream_stand = IceCreamStand("Ice Dream", "Ice Cream Parlor")

# Displaying available flavors 
ice_cream_stand.display_flavors()