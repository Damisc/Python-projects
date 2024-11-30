# Ask the user for their name and the other person's name.
print("Welcome to the Love Calculator.")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# need to combine the two names and change them to lower case.
combined_names = name1.lower() + name2.lower()
print(combined_names)

# Get the amount of times the individual letters in "true" occur in the combined_names.
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

# Get the amount of times the individual letters in "love" occur in the combined_names.
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

# Combine the total of both as strings.
total_true = str(t + r + u + e)
total_love = str(l + o + v + e)

# Convert the result back into integers.
total_score = int(total_true + total_love)

# Check the conditions and output the result.
if (total_score < 10) or (total_score > 90):
    print(f"Your score is {total_score}, you go together like coke and mentos.")

elif (total_score >= 40) and (total_score <= 50):
    print(f"Your score is {total_score}, you are alright together.")

else:
    print(f"Your score is {total_score}")
