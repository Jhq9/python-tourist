cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)
# 根据字符串的首字母排序
print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# reverse()方法只是反转列表元素的排列顺序
# reverse()方法是永久性地修改列表元素的排列顺序
cars.reverse()
print(cars)

# len()方法获取列表的长度
print(len(cars))


