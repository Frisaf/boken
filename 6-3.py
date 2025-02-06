import random

numbers = []

for i in range(0, 100):
    numbers.append(random.randint(1, 1000))

print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers)/len(numbers))