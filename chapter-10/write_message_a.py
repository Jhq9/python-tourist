# 以附加的模式打开文件，并在末尾添加新的内容

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in the large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")