def is_disarium(num):
    return num == sum(int(d)**(i+1) for i, d in enumerate(str(num)))

num = 135
if is_disarium(num):
    print(num, "is a Disarium number")
else:
    print(num, "is not a Disarium number")
