def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d**power for d in digits)

num = 153
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
