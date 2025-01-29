import math

λ = math.log(2) / 5730
t = int(input("> "))
n = 100 * math.e ** (-λ * t)

print(f"{n:.1f}%")