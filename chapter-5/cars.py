cars = ['audi', 'bmw', 'subaru', 'toyota']

# if 语句也是类似for语句的缩进控制
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# 可检测某个值是否在列表中
print('bmw' in cars)