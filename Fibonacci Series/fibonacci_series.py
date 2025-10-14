def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b

n = 10
print("Fibonacci Series up to", n, "terms:")
fibonacci(n)
