# 首字母大写表示的是类
class Dog():
    # 一个特殊的方法，实例化的时候会默认调用，形参self必不可少，必须在第一个(它是指向实例本身的一个引用，让实例能够访问类中的属性和方法)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolling over!")


my_dog = Dog('may', 12)
your_dog = Dog('lucy', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

your_dog.roll_over()
your_dog.sit()