print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
choice = input('You\'re at a cross road. \n Where do you want to go? Type "Left" or "Right".').lower()
if choice =="left":
    # You want to continue the game
    choice2 = input("You've come to a lake, there is an island in the middle of the lake.\n"
                "Type 'wait' to wait for boat or type 'swim' to swim across. ").lower()
    if choice2== "Wait":
       choice3 = input("You arrive at the island unharmed. There is house with 3 doors.\n One red"
             "one blue, one yellow which color will you choose?").lower()
       if choice3 == "red":
             print("It's room of full fire. Gameover")
       elif choice3 == "yellow":
             print("You've the treasure. You Win!")
       elif choice3 == "blue":
             print("You enter a room of beast. Gameover")
       else:
             print("You chose a door that doesn't exist. Game Over")
    else:
        print("You have got attacked by trout. Game Over")
else:
    print("You went to the right side. Game Over")