def is_spy(num):
    digits = [int(d) for d in str(num)]
    return sum(digits) == __import__('functools').reduce(lambda x,y:x*y, digits, 1)

num = 123
if is_spy(num):
    print(num, "is a Spy number")
else:
    print(num, "is not a Spy number")
