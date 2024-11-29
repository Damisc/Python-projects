# print a welcome message
print("Welcome to the tip calculator.")

# Ask for the total bill
total_bill = input("What is the total bill? $")

# Ask for the percentage of tip they would like to give
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")

# Ask for the amount of people splitting the bill
split = input("How many people to split the bill? ")

# Calculation
total_tip = float(total_bill) * (int(tip)/100)
each_pay = round((float(total_bill) + total_tip) /int(split), 2)

# Print the output
print(f"Each person should pay: ${each_pay}")
