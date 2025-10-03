def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

n = 50
print("Prime numbers between 1 and", n, ":")
for i in range(1, n+1):
    if is_prime(i):
        print(i, end=" ")
