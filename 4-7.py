import sys

judges = []

while True:
    try:
        judge_inp = int(input("How many judges?\n> "))

        if judge_inp < 3:
            print("The amount of judges has to be 3 or greater.")
        
        else:
            for i in range(0, judge_inp):
                judge_name = f"judge_{i+1}"

                judges.append(judge_name)
            
            break
    
    except ValueError:
        print("Please enter an integer")

judge_points = {}

while True:
    try:
        level = int(input("Which difficulty level? Enter a negative number to exit\n> "))

        if level < 0:
            sys.exit()
    
    except ValueError:
        print("You need to enter an integer")

    judge_scoring = []

    for i in range(0, len(judges)):
        while True:
            scoring = int(input(f"Points from judge {i+1}: "))

            if scoring < 0:
                sys.exit()

            elif 0 <= scoring <= 10:
                judge_scoring.append(scoring)
                break

            else:
                print("Please enter an integer between 0 and 10.")

    for i in judge_scoring:
        print(i)

    judge_scoring.remove(min(judge_scoring))
    judge_scoring.remove(max(judge_scoring))

    score = (sum(judge_scoring)/len(judge_scoring)) * 3 * level

    print(score)