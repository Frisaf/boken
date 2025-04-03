import random

li = [
    [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
    [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
    [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
    [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
]

magic_square = True
count = 0

print(li)

for i in range(0, len(li)):
    x = li[i]
    y = []
    y.append(x[count])
    z = sum(y)

    if x != y:
        magic_square = False

if magic_square == True:
    print("It's a magic square!")

else:
    print("It's not a magic square :(")