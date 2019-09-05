prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you finished)"

# break语句可以退出循环，同样适用于for循环
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("I'd love to go to " + message.title() + "!")
