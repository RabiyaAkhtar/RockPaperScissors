
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("\nLet's play ROCK, PAPER, SCISSORS!\n")

user_score = 0
computer_score = 0

while True:
    while True:
        user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")

        if user_choice.isdigit():
            user_choice = int(user_choice)

            if 0 <= user_choice < len(game_images):
                break
            else:
                print("Invalid choice. Please enter a valid number (0, 1, or 2).")
        else:
            print("Invalid input. Please enter a valid number (0, 1, or 2).")

    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == 0 and computer_choice == 2) or
        (user_choice == 1 and computer_choice == 0) or
        (user_choice == 2 and computer_choice == 1)
    ):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Your Score: {user_score}, Computer Score: {computer_score}")

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again != 'yes':
        break
