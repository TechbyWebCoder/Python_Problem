def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

num = 28
if is_perfect(num):
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")
