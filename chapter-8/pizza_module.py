def make_pizza(*toppings):
    print(toppings)
    print("\nMake a pizza with the following toppings: ")
    for topping in toppings:
        print("-" + topping)


# 可接受任意数量的形参必须放在后面，在默认参数的前面
def make_size_pizza(size, *toppings):
    print("\nMake a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("-" + topping)
