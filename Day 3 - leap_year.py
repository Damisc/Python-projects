# Ask the user for the year they would like to check
year = int(input("Which year do you want to check? "))

# Check and output if the year entered is a leap year or not
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
