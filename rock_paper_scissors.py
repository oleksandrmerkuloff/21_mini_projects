import random


figures = ["rock", "paper", "scissors"]

computer_score = 0
player_score = 0

user_name = input("Enter your name: ")

while True:
    computer_figure = random.randint(0, 2)
    print(f"{user_name}: {player_score} vs Computer: {computer_score}")

    player_figure = input("Enter your figure(0-rock, 1-paper, 2-scissors): ")
    if player_figure.lower() == "exit":
        print(f"Your final score: {player_score} vs computer: {computer_score}.")
        break

    try:
        player_figure = int(player_figure)
    except ValueError:
        print("Unknown figure, try again!")
        continue

    if 0 > player_figure or player_figure > 2:
        print("Unknown figure, try again!")
        continue

    if computer_figure == player_figure:
        print(f"You both choose {figures[player_figure]}.\nIt's a draw!")
        continue
    print(f"You choose: {figures[player_figure]} and Computer choose: {figures[computer_figure]}")
    if ((computer_figure == 0 and player_figure == 1) or
       (computer_figure == 1 and player_figure == 2) or
       (computer_figure == 2 and player_figure == 0)):
        player_score += 1
        print("You win!")
    else:
        computer_score += 1
        print("You lose...")
