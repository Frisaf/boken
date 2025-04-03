import random

matrix = []
matrix_item = []

matrix_item += ["B"] * random.randint(0, 100)
matrix += matrix_item * random.randint(0, 100)

columns = len(matrix)
rows = len(matrix_item)
symmetric = True

for i in range(0, columns):
    for j in range(0, len(matrix[i])):
        try:
            if columns != rows and matrix[i][j] != matrix[j][i]:
                print("Not symmetrical")
                symmetric = False
        
        except IndexError:
            symmetric = False

if symmetric == True:
    print("Symmetrical!")

else:
    print("Not symmetric")