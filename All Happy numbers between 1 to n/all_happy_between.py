def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(d)**2 for d in str(num))
    return num == 1

n = 50
print("Happy numbers between 1 and", n, ":")
for i in range(1, n+1):
    if is_happy(i):
        print(i, end=" ")
