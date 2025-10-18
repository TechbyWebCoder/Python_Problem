def is_neon(num):
    sq = num * num
    return sum(int(d) for d in str(sq)) == num

num = 9
if is_neon(num):
    print(num, "is a Neon number")
else:
    print(num, "is not a Neon number")
