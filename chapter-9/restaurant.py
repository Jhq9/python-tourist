class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ", and its cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is opening!")

hotel_restaurant = Restaurant('Jay', 'hotel')

hotel_restaurant.describe_restaurant()
hotel_restaurant.open_restaurant()