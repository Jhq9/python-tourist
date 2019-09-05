# 函数input()让程序暂停运行，等待用户输入一些文本。获取到用户输入后，Python将其存储在一个变量中
prompt = "\nTell me something, and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


