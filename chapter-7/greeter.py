name = input("Please enter your name: ")

print("Hello, " + name + "!")


prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")


# input()方法将用户输入解析为字符串，int()方法将输入解析为数值

age = input("How old are you? ")
age = int(age)
print(age)