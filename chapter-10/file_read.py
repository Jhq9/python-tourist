# open()的文件路径可以是相对路径，也可以是绝对路径
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


file_name = 'pi_digits.txt'

# 逐行读取
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())


# 创建一个包含文件各行内容的列表lines
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())