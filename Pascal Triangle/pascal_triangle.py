def pascal(n):
    for i in range(n):
        print(" "*(n-i), end="")
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            num = num * (i-j) // (j+1)
        print()

n = 5
pascal(n)
