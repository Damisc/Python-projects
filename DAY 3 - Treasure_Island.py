# Printing some welcome message

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Treasure Island. \nYour mission is to find the treasure")

# Asking the user for input and checking the conditions to give the appropriate output
first_move = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if first_move == "right":
    print("You were killed by a wild bear. Game Over.")
elif first_move == "left":
    # continue in the game
    second_move = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if second_move == "swim":
        print("You were eaten by a crocodile. Game Over.")
    elif second_move == "wait":
        # continue in the game
        third_move = input("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow, and one blue. Which colour do you choose? \n")
        if third_move == "red":
            print("You ran into the room. There was a fire and you burned. Game Over.")
        elif third_move == "blue":
            print("There was a bull waiting on the otherside, Yoou were crushed. Game Over.")
        elif third_move == "yellow":
            print("You entered the house where the treasures were hidden, You are going to be rich. You Won.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

