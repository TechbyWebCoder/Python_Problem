def evil_or_odious(num):
    count_ones = bin(num).count("1")
    return "Evil" if count_ones % 2 == 0 else "Odious"

num = 15
print(num, "is", evil_or_odious(num), "number")
