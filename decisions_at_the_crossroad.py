number = int(input("Enter a number: ")) #added int to make sure the input converted the string to an integer

if number > 0:
    print("The number is positive.")
elif number == 0: #added another = to make sure the program new that the input had to be equal to 0 instead of setting number to 0
    print("The number is zero.")
else: #Deleted number < 0 because it was not necessary for the else function
    print("The number is negative.")