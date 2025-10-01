def is_automorphic(num):
    return str(num*num).endswith(str(num))

n = 1000
print("Automorphic numbers between 1 and", n, ":")
for i in range(1, n+1):
    if is_automorphic(i):
        print(i, end=" ")
