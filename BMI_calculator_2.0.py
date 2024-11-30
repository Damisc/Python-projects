# ask the user for their height and weight

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Calculate the BMI
BMI = round(weight / height ** 2)

# Output the result in a more understandable way
if BMI < 18.5:
    print(f"Your bmi is {BMI},you are underweight.")
elif BMI < 25:
    print(f"Your bmi is {BMI}, You have a normal weight.")
elif BMI < 30:
    print(f"Your bmi is {BMI}, You are overweight")
elif BMI < 35:
    print(f"Your bmi is {BMI}, You are obese.")
else:
    print(f"Your bmi is {BMI}, You are clinically obese.")
