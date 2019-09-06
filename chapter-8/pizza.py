# *toppings表示可传递任意数量的实参，*topping的星号让Python创建一个名为toppings的元组
def make_pizza(*toppings):
    print(toppings)
    print("\nMake a pizza with the following toppings: ")
    for topping in toppings:
        print("-" + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 可接受任意数量的形参必须放在后面，在默认参数的前面
def make_size_pizza(size, *toppings):
    print("\nMake a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("-" + topping)

