def is_spy(num):
    digits = [int(d) for d in str(num)]
    return sum(digits) == __import__('functools').reduce(lambda x,y:x*y, digits, 1)

n = 200
print("Spy numbers between 1 and", n, ":")
for i in range(1, n+1):
    if is_spy(i):
        print(i, end=" ")
