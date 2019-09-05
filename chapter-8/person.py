# 返回字典类型
def build_person(first_name, last_name):
    person = {'first_name': first_name, 'last_name': last_name}
    return person

print(build_person('jin', 'huaquan'))


def build_person_age(first_name, last_name, age = ''):
    person = {'first_name': first_name, 'last_name' : last_name}
    if age:
        person['age'] = age
    return person

print(build_person_age('Jin', 'Huaquan'))
print(build_person_age('Jin', 'Huaquan', '18'))