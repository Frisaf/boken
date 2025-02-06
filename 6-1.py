k = 3
numbers = [2]
max = int(input("How many times should it run?\n> "))
run = 0
error = False

while run < max:
    try:
        current = numbers[len(numbers) - 1]
        next = current * k

        numbers.append(next)
        print(next)
        run += 1
    
    except ValueError as e:
        print(e)
        print("Quitting...")
        error = True
        run = max

print("Final result:")

if error == True:
    final = []

    for i in range(0, len(numbers) - 1):
        final.append(numbers[i])

    print(final)

else:
    print(numbers)