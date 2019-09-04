# range(start, end) 生成数字一系列，而非列表，值不包括end
for value in range(1, 5):
    print(value)

# list()方法将range()的数字序列转换为列表
numbers = list(range(1, 6))
print(numbers)


# range方法还可以指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Python里**表示乘方
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
