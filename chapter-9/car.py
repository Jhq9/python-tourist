class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, odometer_reading):
        if odometer_reading > self.odometer_reading:
            self.odometer_reading = odometer_reading
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 直接修改实例的属性值
my_new_car.odometer_reading = 20
my_new_car.read_odometer()

# 调用方法修改属性值
my_new_car.update_odometer(10)
my_new_car.read_odometer()


# 调用方法增值
my_new_car.increment_odometer(20)
my_new_car.read_odometer()
