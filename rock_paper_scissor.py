import random

choices_option = ('r', 'p', 's')

while True:
    user_choice = input("Rock/Paper/Scissor (r/p/s) : ").lower()
    if user_choice not in choices_option:
        print("Invalid chioce")
    computer_choice = random.choice(choices_option)
    print(f'You choose {user_choice} and computer choose {computer_choice}')
    if user_choice == computer_choice:
        print("DRAW")
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
        print("YOU WIN")
    else:
        print("YOU LOOSE")
    wanna_continue = input("Do you want to continue?(y/n) : ")
    if wanna_continue == 'n':
        print("Thanks for playing!!")
        break
