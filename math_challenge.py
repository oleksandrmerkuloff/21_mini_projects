import random
import time


MIN_VALUE = 1
MAX_VALUE = 10
OPERATORS = ['+', '-', '*']


def generate_problem():
    right = random.randint(MIN_VALUE, MAX_VALUE)
    left = random.randint(MIN_VALUE, MAX_VALUE)
    operator = random.choice(OPERATORS)

    expression = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expression)
    return expression, answer


score = 0
lives = 3
start_time = time.time()

print("Game started!")
while lives > 0:
    print("You have 3 lives")
    new_exp, answer = generate_problem()
    print("Your score: " + str(score))
    print(new_exp)
    user_guess = int(input("Your answer is: "))
    if user_guess == answer:
        score += 1
    else:
        lives -= 1

finish_time = time.time() - start_time

print("Good job! Your final score: " + str(score))
print("Your time: %.2f sec" % finish_time)
