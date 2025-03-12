while True:
    try:
        tests = int(input("How many tests?\n> "))
        break
    
    except ValueError:
        print("Enter a number instead.")

print("Press enter when you are done.")

names = []
scores = []
student_scores = []
count = 0

while True:
    student_name = input("Student name: ")

    if student_name == "":
        break

    else:
        names.append(student_name)
        student_scores.append([])
        student_scores[count].append(student_name)

        for i in range(tests):
            while True:
                try:
                    test_score = int(input(f"{student_name}'s score for test {i+1}: "))
                    scores.append(test_score)
                    break
                
                except ValueError:
                    print("Enter a number instead.")

        for i in range(len(scores)):
            student_scores[count].append(scores[i])

        count += 1
        scores.clear()

student_avg = []

for item in student_scores:
    for x in item:
        if type(x) == str:
            name = x
        
        elif type(x) == int:
            student_avg.append(x)
    
    print(f"{name}'s average score: {sum(student_avg)/len(student_avg)}")

    student_avg.clear()

for i in range(tests):
    total_scoring = 0

    for a in range(len(names)):
        total_scoring += student_scores[i][a+1]
    
    avg = total_scoring/len(names)

    print(f"Average score for test {i+1}: {avg}")