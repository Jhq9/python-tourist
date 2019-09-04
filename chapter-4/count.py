for number in range(1, 21):
    print(number)

numbers = [value for value in range(1, 1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = [number for number in range(1, 20, 2)]
print(odd_numbers)

three_numbers = [number for number in range(3, 31, 3)]
print(three_numbers)

third_numbers = [number ** 3 for number in range(1, 11)]
for number in third_numbers:
    print(number)
print(third_numbers)