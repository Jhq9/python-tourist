# for循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to your next trick," + magician.title() +"\n")
# 因为这行的缩进不在for循环中，只执行一次
print("Thank you, everyone, That was a great magic show!")

