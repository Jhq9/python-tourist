# 异常 Error,异常是使用 try-except代码块处理的
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and i'll divide them")

# try-except-else 代码块
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
