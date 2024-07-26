x = int(input("What is the first number? "))
y = int(input("What is the second number? "))
z = int(input("What is the third number? "))

if x >= y and x >= z:
    print("The largest number is", x)
elif y >= x and y >= z:
    print("The largest number is", y)
else:
    print("The largest number is", z)

if x <= y and x <= z:
    print("The smallest number is", x)
elif y <= x and y <= z:
    print ("The smallest number is", y)
else:
    print ("The smallest number is", z)