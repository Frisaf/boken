import math

a = float(input("Sida 1: "))
b = float(input("Sida 2: "))
alfa = math.radians(float(input("Vinkel alfa: ")))
c = math.sqrt((a**2) + (b**2) - (2*a*b*math.cos(alfa)))

if abs(a-b) < 10**-10 and abs(b-c) < 10**-10 and abs(c-a) < 10**-10:
    print("Liksidig")
elif  abs(a-b) < 10**-10 or abs(b-c) < 10**-10 or abs(c-a) < 10**-10:
    print("Likbent")

elif a != b and b != c and c != a:
    print("Oliksidig")