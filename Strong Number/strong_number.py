import math

def is_strong(num):
    return num == sum(math.factorial(int(d)) for d in str(num))

num = 145
if is_strong(num):
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")
