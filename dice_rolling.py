import random
# count = int(input("How many times do you want to roll the dice? "))
# for i in range(count):
while True:
    choice = input("Do you wanna roll the dice? (Yes/No): ")
    if choice == "Y" or choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'(You rolled {dice1} and {dice2})')
    elif choice == "N" or choice == "n":
        print("Okay, maybe next time!")
        break
    else:
        print("Invalid input. Please enter Y or N.")
