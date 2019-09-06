filename = 'programming.txt'

# 第二个实参表示已写入的方式打开文件('w'), 'r'标识以读的方式默认方式, 'r+'读取加写入，'a'附加模式
# 如果你要写入的文件不存在，函数open()将自动创建它。然而，以写入（'w'）模式打开文件时千万要小心，
# 因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    # 写入多行
    file_object.write("I love creating new games.\n")