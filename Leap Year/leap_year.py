def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = 2024
if is_leap(year):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
