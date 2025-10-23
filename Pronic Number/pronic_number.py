def is_pronic(num):
    for i in range(num+1):
        if i*(i+1) == num:
            return True
    return False

num = 20
if is_pronic(num):
    print(num, "is a Pronic number")
else:
    print(num, "is not a Pronic number")
