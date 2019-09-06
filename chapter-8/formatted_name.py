# 让实参变得可选  给形参指定默认值时，等号两边不要有空格：

def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()


print(get_formatted_name("jin", "huaquan"))


def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
