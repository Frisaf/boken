number = input("Personnummer: ")
first = number[:-5]
last = number[9:]
control = number[:-1]
real_control = control.replace("-", "")
numbers = []
a = []

for letter in real_control:
    numbers.append(int(letter))

for i in range(0, len(numbers), 2):
    a.append(numbers[i])

    numbers[i] = ""

for item in numbers:
    if item == "":
        numbers.remove(item)

for num in numbers:
    a.append(num * 2)

for num in a:
    