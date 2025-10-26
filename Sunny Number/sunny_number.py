import math

def is_sunny(num):
    return math.isqrt(num+1)**2 == num+1

num = 8
if is_sunny(num):
    print(num, "is a Sunny number")
else:
    print(num, "is not a Sunny number")
