# Python中不可变的列表称为元祖，不能给元祖的元素赋值
dimensions = (200, 500)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)
    
# 虽然不能修改元祖的元素，但可以重新给存储元祖的变量赋值
dimensions = (100, 400)
print(dimensions[0])
print(dimensions[1])