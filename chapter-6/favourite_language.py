favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# 字典调用items()返回键值对的列表
for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title())

# 字典调用keys()只返回所有的key列表,直接遍历字典等同于默认遍历key列表
for name in favourite_languages:
    print(name.title())

for name in favourite_languages.keys():
    print(name.title())

# 字典调用values()返回所有的value列表
for language in favourite_languages.values():
    print(language)

# 封装成set可以去重
for language in set(favourite_languages.values()):
    print(language)


print("Sarah's favourite language is " +
      favourite_languages['sarah'].title() +
      ".")


john_info = {
    'first_name': 'john',
    'last_name': 'edward',
    'city': 'new york'
}
print(john_info['first_name'])
print(john_info['last_name'])
print(john_info['city'])


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

# 用for循环遍历字典的key-value
for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: " + value)


