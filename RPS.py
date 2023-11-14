
import random
choices = ['rock', 'paper', 'scissors']
while True:
    user_choice = input('Select choice (rock, paper or scissors): ')
    comp_choice = random.choice(choices)
    print(f"Your choice {user_choice}, computer choice {comp_choice}\n")
    if user_choice == comp_choice:
        print(f" It's a tie!")
    elif user_choice == "rock" and comp_choice =="scissors":
        print("you win!")
    elif user_choice == "paper" and comp_choice =="rock":
        print("You Win!")
    elif user_choice == "scissors" and comp_choice =="paper":
        print("You Win!")
    else:
        print("Computer Wins!")
            
    play_again = input('Play again? (yes/no)')
    if (play_again.lower() == 'n'):
        break
