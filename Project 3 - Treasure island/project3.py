print(r"""
                   *       .        *       .       *
             .         *       .        *      .
         *       .                  *               .     *

              . *        .      *        .       *

        .-=================================================-.
       /| .-------------------------------------------------. |\
      / | |  *    *    *    *    *    *    *    *    *    *  | | \
     /  | |  *    *    *    *    *    *    *    *    *    *  | |  \
    /   | '---------------------------------------------------' |   \
   /    |  _________________________________________________    |    \
  /   .-|-[_________________________________________________]-. |     \
 /   /  | |                                                   | |  \   \
|   /   | |   .----.  .----.  .----.  .----.  .----.  .---.  | |   \   |
|  /    | |  ( GOLD )( GOLD )( GOLD )( GOLD )( GOLD )(GOLD)  | |    \  |
| /     | |   '----'  '----'  '----'  '----'  '----'  '---'  | |     \ |
|/      | |  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  * | |      \|
|       | |___________________________________________________|/|       |
|       |.-===================================================.||       |
|       ||  |=========================================|       |||       |
|       ||  |  T  R  E  A  S  U  R  E    C  H  E  S  T  |   |||       |
|       ||  |=========================================|       |||       |
|       ||.-[_______________________(@)_______________]-.|    |||       |
|       |'---------------------------------------------------'||       |
|       '-----------------------------------------------------'|       |
|        \___________________________________________________/ |       |
 \        |      .-------------------------------.      |      /
  \       |     / .---.                   .---. \      |     /
   \      |    | ( $$$ )   X   X   X     ( $$$ ) |     |    /
    \     |     \ '---'   X   X   X   X   '---' /      |   /
     \    |      '-------------------------------'      |  /
      \   |_______________________________________________|/
       \  /  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~   \/
        \/___________________________________________________/
""")

print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake, there is an island in the middle of the lake.' \
                    ' Type "wait" to wait for a boat. Type "swim" to swim across the lake').lower()
    
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ').lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You were attacked by an angry trout. Game Over.")
    
else:
    print("You fell in a hole. Game Over.")
    






