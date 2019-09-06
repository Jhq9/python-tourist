def build_profile(first, last, **user_info):
    print(user_info)
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


# 两个**修饰的形参表示传递的是任意数量的key-value的字典属性
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
