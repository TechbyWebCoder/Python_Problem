def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = 6
print("Factorials from 1 to", n, ":")
for i in range(1, n+1):
    print(i, "->", factorial(i))
