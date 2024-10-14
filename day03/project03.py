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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
choice1 = input('You are at a crossroad, where do you want to go?\n '
                'Type "left" or "right" to continue.\n').lower()

if choice1 == "left":
    choice2 = input('You found a lake. '
                    'There is an Island in the middle of it. '
                    'Type "wait" to wait for a boat or type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed.\n"
              "There is a house and you decided to enter in it.\n "
              "The house has three doors. One red, one yellow and another one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("Oh no! You dropped a candle and started a fire! Game Over.")
        elif choice3 == "yellow":
            print("Congratulations! You found the treasure!")
        elif choice3 == "blue":
            print("You have come across a lair of wild and hungry beasts and there is no way to escape. Game Over.")
        else:
            print("This is not a valid answer. Game Over.")
    else:
        print("You we're attacked by a giant trout! Game Over.")
else:
    print("You're walking down the road until you fall into a hole. Game Over.")

