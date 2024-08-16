import random

game_list = ["rock", "paper", "scissors"]

print("Hey👋.\nWelcome To RockPaperScissors Game!\nC'mon let's see who the champion is!")
user_name = input("What is your name?: ")
print(f"Hey {user_name}")

def game():
    user_input = input("What do you want to choose? (rock/paper/scissors): ")
    comp_choice = random.choice(game_list)
    win = None
    print(f"Computer chooses : {comp_choice}")

    if comp_choice == user_input:
        print("Oh No!, It's a Tie")
        return


    if (comp_choice == "rock" and user_input == "paper") or (comp_choice == "paper" and user_input == "scissors") or (comp_choice == "scissors" and user_input == "rock"):
        win = True
    else:
        win = False


    if win:
        print(f"Wohooo! {user_name} you win!🎉")
    else:
        print(f"Oh no, {user_name} you lose.😌\nComputer wins")

while True:
    game()
    ask = input("Do you want to continue? (yes/no): ")
    if ask.lower() != "yes":
        print("\n")
        print("Thanks for playing! Goodbye!👋")
        break









