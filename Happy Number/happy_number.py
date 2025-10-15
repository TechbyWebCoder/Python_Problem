def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(d)**2 for d in str(num))
    return num == 1

num = 19
if is_happy(num):
    print(num, "is a Happy number")
else:
    print(num, "is not a Happy number")
