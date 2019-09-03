motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 修改列表的某个元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表的最后面添加一个元素
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表的任意位置插入元素.
motorcycles.insert(1, 'ducati')
print(motorcycles)

# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续使用它，就使用方法pop()。


# 删除某个元素 del
del motorcycles[1]
print(motorcycles)

# 删除列表的最后一个元素 pop(), pop()返回从列表中删除的值
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

print("The last motorcycle i owned was a " + poped_motorcycle.title() + ".")

# 弹出(删除)列表中任意位置的元素
motorcycles.append(poped_motorcycle)
poped_motorcycle = motorcycles.pop(0)
print("The first motorcycle i owned was a " + poped_motorcycle.title() + ".")

# 根据值删除元素
motorcycles.remove('yamaha')
print(motorcycles)

# 元素值可重复
motorcycles.append('yamaba')
motorcycles.append('yamaba')
print(motorcycles)