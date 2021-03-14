import random

computer_score = 0
human_score = 0
print("Welcome to the rock paper scissor game!")
answer = input("Do you want to play? ").casefold()

if answer == "yes":
    while True:
        computer_choice = random.randint(1, 3)
        human_choice = int(input("Choose a number from 1 to 3\n1 is rock\n2 is paper\nand 3 is scissors\n"))
        print()
        if computer_choice == 1 and human_choice == 1:
            print("it's a draw")
            print(f"The computer picked {computer_choice}")

        elif computer_choice == 1 and human_choice == 2:
            print("You get a point")
            human_score += 1
            print(f"The computer picked {computer_choice}")

        elif computer_choice == 1 and human_choice == 3:
            print("Computer gets a point")
            computer_score += 1
            print(f"The computer picked {computer_choice}")

        elif computer_choice == 2 and human_choice == 1:
            print("Computer gets a point")
            computer_score += 1
            print(f"The computer picked {computer_choice}")

        elif computer_choice == 2 and human_choice == 2:
            print("It's a draw")
            print(f"The computer picked {computer_choice}")

        elif computer_choice == 2 and human_choice == 3:
            print("you get a point")
            human_score += 1
            print(f"The computer picked {computer_choice}")

        elif computer_choice == 3 and human_choice == 1:
            print("You get a point")
            human_score += 1
            print(f"The computer picked {computer_choice}")

        elif computer_choice == 3 and human_choice == 2:
            print("Computer gets a point")
            computer_score += 1
            print(f"The computer picked {computer_choice}")

        elif computer_choice == 3 and human_choice == 3:
            print("it's a draw")
            print(f"The computer picked {computer_choice}")

        if computer_score == 3:
            print("You lost better luck next time")

        elif human_score == 3:
            print("You won, wow you are good")
        print(f"You have {human_score} wins and "
              f"the Computer has {computer_score} wins")
        print()
else:
    print("Ok then see you around")
