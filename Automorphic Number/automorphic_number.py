def is_automorphic(num):
    return str(num*num).endswith(str(num))

num = 25
if is_automorphic(num):
    print(num, "is an Automorphic number")
else:
    print(num, "is not an Automorphic number")
