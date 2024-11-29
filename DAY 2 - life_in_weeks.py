# ask the user for the age
age = input("Waht is your current age? ")
end_age = input("What is the end age? ")

# calculate the days, weeks, months we have left if we live until the end age
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

years_remaining = int(end_age) - int(age)

days_left = years_remaining * 365
weeks_left = years_remaining * 52
months_left = years_remaining * 12

# Print the output
output = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(output)
