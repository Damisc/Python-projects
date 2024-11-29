# Ask the user for their height and weight
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# Calculate the BMI
BMI = int(weight) / float(height) ** 2

# Print the output
print(int(BMI))

