# Quiz game on ten question about Harry Potter

scoreboard = {}

questions = {
    "What is the first chapter of the first book?": "The Boy Who Lived",
    "Who destroyed the ring horcrux?": "Dumbledore",
    """Which fake illness does Ron Weasley say he has to cover up his absence
from Hogwarts in their seventh year?""": "Spattergroit",
    "On what date did the Battle of Hogwarts end with Voldemort's death?(month day, year)": "May 2, 1998",
    "How many classes did Hermione Granger take in her third year?": "12",
    """Lily Potter once gave Professor Slughorn a bowl with a lily that turned into a goldfish.
What was the goldfish's name?""": "Francis",
    "Which two students came up with the name \"Dumbledore's Army\"?": "Cho and Ginny",
    "What's the longest movie in the series? (write full film name)": "Harry Potter and the Chamber of Secrets",
    "True or false: Hermione is younger than Ron and Harry.": "False",
    "Which two creatures are Hippogriffs a mix of?": "Horse and Eagle"
}

print("Welcome to the Harry Potter Quiz!")
print("""
    The game has three command:
    1 - if you want to play print 'start';
    2 - if you want to check your rating print 'scoreboard';
    3 - if you want to leave print 'exit';
    Have fun and will be the best
""")

player_name = input("Write your name: ")

while True:
    mode = input("Wait for a command: ").lower()

    if mode == "exit":
        print("See you soon!)")
        break
    elif mode == "scoreboard":
        if scoreboard:
            for name, score in scoreboard.items():
                print(f"{name}: {score}")
        else:
            print("Doesn't have a players in scoreboard, be first!")
    elif mode == "start":
        score = 0
        for quiz, answer in questions.items():
            player_anwer = input(quiz + ":\n").lower()
            if player_anwer == answer.lower():
                score += 1
        if player_name in scoreboard.keys():
            if score > scoreboard[player_name]:
                scoreboard[player_name] = score
        else:
            scoreboard[player_name] = score
        if score == 10:
            print("You're truly Harry Potter fan our congrats!")
        elif score >= 5:
            print(f"Good job, you have {score}/10!")
        elif score < 5:
            print(f"Not bad but not good, you have {score}/10.") 
        after_game = input("Do you want to continue 'y/n' if player will be changed print 'yy': ").lower()
        if after_game == "n":
            print("It was fun see ya!")
            break
        elif after_game[0] == "y":
            if after_game == "yy":
                player_name = input("Write your name: ")
        else:
            print("Unknown command error...")
            break
    else:
        print("unknown command try again")
