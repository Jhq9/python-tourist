# 函数的参数为列表
def greet_users(names):
    for name in names:
        msg = 'Hello,' + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']

greet_users(usernames)