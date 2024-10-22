import random

modes = {
    1: 10,
    2: 5,
    3: 3
}

print("""Welcome in the number guesser in this game you have three mods:
      1 - easy (10 lives);
      2 - normal (5 lives);
      3 - hard (3 lives);
Choose your mode and start play!""")

while True:
    mode = int(input("Enter your mode: "))
    lives = modes[mode]
    hidden_num = random.randint(1, 100)

    for _ in range(lives):
        print(f"You have {lives} lives")
        player_number = int(input("Enter your number: "))
        if player_number == hidden_num:
            print("Good job, you find it!")
            hidden_num = 0
            break
        elif player_number > hidden_num:
            print("Too high!")
        elif player_number < hidden_num:
            print("Too low")
        lives -= 1

    if hidden_num:
        print(f"Almost done, but youre number was {hidden_num}")

    new_game = input("If you want to continue or exit print 'y/n': ").lower()
    if new_game == "n":
        print("Good playing! See ya!")
        break
