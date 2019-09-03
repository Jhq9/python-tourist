# 列表(数组) 元素的索引从0开始
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())

# Python为访问最后一个元素提供了一个特殊的语法。通过索引-1，可让Python返回最后一个列表元素
print(bicycles[-1])  # specialized
print(bicycles[-2])  # redline


message = "My first bicycle is a " + bicycles[0].title() + "."
print(message)
