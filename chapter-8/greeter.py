def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print('\nPlease tell me name:')

    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello," + formatted_name + "!")
# 定义函数
def greet_user():
    print("Hello!")

# 调用函数
greet_user()

# 没有重载，username表示形参，而传入的'May'为实参
def greet_user_username(username):
    print("Hello, " + username.title() + "!")

greet_user_username("May")
