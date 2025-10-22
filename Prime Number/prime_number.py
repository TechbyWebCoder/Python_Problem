num = 29
if num > 1:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(num, "is not Prime")
            break
    else:
        print(num, "is Prime")
else:
    print(num, "is not Prime")
