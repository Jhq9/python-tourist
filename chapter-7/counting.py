# while循环
current_number = 1
while current_number < 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something. and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program"

message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
