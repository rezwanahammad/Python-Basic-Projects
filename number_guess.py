import random

number_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter number between 1 and 100 : "))
        if guess < number_guess:
            print("Low")
        elif guess > number_guess:
            print("High")
        else:
            print("Congratulations!You've guessed the right number")
            break
    except:
        print("Enter valid number please")

print("Happy Guessing..!!")
