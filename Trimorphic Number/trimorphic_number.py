#Trimorphic Number

def is_trimorphic(num):
    return str(num**3).endswith(str(num))

num = 24
if is_trimorphic(num):
    print(num, "is a Trimorphic number")
else:
    print(num, "is not a Trimorphic number")
