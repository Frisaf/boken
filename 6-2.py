import random

while True:
    try:
        x = int(input("How many numbers?\n> "))
        break

    except ValueError:
        print("Please provide a number instead.")

numbers = []

for i in range(0, x):
    numbers.append(random.randint(-10000, 10000))

count = 0

for number in numbers:
    if number < 0:
        count += 1

print(count)