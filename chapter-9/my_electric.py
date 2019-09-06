# 从一个模块中导入多个类
from electric_car import ElectricCar, Car

my_tesla = ElectricCar('tesla', 'model s', 2017)

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
