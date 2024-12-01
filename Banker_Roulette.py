# import the random module
import random

# Get the name of everybody
people_names = input("Give me everybody's names, seperated by a coma: ")
names = people_names.split (", ")

# get the total number of names in list.
number_of_people = len(names)

# generate random numbers between 0 and the last index.
person_to_pay = random.randint(0, (number_of_people - 1))
choice = names[person_to_pay]

# Print the output
print(f"{choice} is going to buy the meal today! ")