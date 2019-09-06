# 可以给函数的形参添加默认值属性,又默认值的形参必须放在最后
def describe_pet(animal_type, pet_name = "Lizy"):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 位置实参
describe_pet("dog", "May")

describe_pet('cat', 'Jay')

# 关键字实参
describe_pet(animal_type='fish', pet_name='rose')

# 关键字实参 参数顺序无所谓
describe_pet(pet_name='rose', animal_type='fish')

describe_pet(animal_type='dog')

describe_pet('cat')

