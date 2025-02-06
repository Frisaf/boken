import random

numbers = []

for i in range(-10000, 10000):
    numbers.append(random.randint(-10000, 10000))

for number in numbers:
    if number == 0:
        numbers.pop(number)

print(len(numbers))