my_foods = ['pizza', 'falafel', 'carrot cake', 'apple', 'banana']
# 利用切片来进行列表的复制,如果直接通过friend_foods = my_foods来进行赋值是引用复制
friend_foods = my_foods[:]
print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

print("The first three items in the list are:")
print(my_foods[0:3])
print("Three items from the middle of the list are:")
print(my_foods[1:4])
print("The last three items in the list are:")
print(my_foods[-3:])
