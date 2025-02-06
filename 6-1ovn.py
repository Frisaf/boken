numbers = []
count = 0

while count < 10:
    x = int(input("Enter a number: "))
    numbers.append(x)
    count += 1

numbers.sort()

for i in range(0, len(numbers)):
    if numbers[i] == numbers[i-1]:
        numbers.pop(i)

for number in numbers:
    print(number)