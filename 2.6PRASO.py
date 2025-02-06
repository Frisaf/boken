import math

t = int(input("år"))
lam = math.log(2)/5730
n = 100*math.e**(-lam*t)
print(n)
