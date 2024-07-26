year = int(input("What year is it? "))

if (year % 4) == 0 and (year % 100) != 0:
    print("This is a leap year.")
elif (year % 400) == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")