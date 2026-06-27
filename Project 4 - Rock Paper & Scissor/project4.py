import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]


user_choice = int(input("What do you want to choose? Type 1 for Rock, 2 for Paper or 3 for Scissors -- ")) 
if user_choice >= 1 and user_choice <= 3:
    print(game_images[user_choice-1])

computer_choice = random.randint(1, 3)
print("Computer Chose : ")
print(game_images[computer_choice-1])

if user_choice >= 4 or user_choice < 1:
    print("You typed an invalid number. You lose!")
elif user_choice == 1 and computer_choice == 3:
    print("You win!")
elif computer_choice == 1 and user_choice == 3:
    print("Computer Wins! You lose...")
elif computer_choice > user_choice:
    print("Computer wins! You lose...")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a Draw!")
