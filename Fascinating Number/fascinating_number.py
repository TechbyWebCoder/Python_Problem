def is_fascinating(num):
    concat = str(num) + str(num*2) + str(num*3)
    return ''.join(sorted(concat)) == "123456789"

num = 192
if is_fascinating(num):
    print(num, "is a Fascinating number")
else:
    print(num, "is not a Fascinating number")
