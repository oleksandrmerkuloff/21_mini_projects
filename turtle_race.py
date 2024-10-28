from random import randint
from turtle import Turtle, Screen


COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
STARTING_POSITIONS = [-600, -400, -200, 0, 220, 420, 620]


class ResultMessage(Turtle):
    result_font = ('Arial', 24, 'bold')

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.goto((-120, 0))

    def write_result(self, winner_color):
        self.write(f'{winner_color.title()} tortoise win!', font=self.result_font)


class Tortoise(Turtle):
    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.setheading(90)


if __name__ == '__main__':
    screen = Screen()
    screen.setup(height=500, width=1400)
    screen.title("Tortoise race!")

    result_board = ResultMessage()

    tortoises = []

    for index in range(7):
        new_racer = Tortoise()
        new_racer.color(COLORS[index])
        new_racer.goto((STARTING_POSITIONS[index], -230))
        tortoises.append(new_racer)

    engine_on = True
    while engine_on:
        for tortoise in tortoises:
            tortoise.forward(randint(10, 20))
            if tortoise.ycor() >= 230:
                result_board.write_result(tortoise.color()[0])
                engine_on = False
                break

    screen.exitonclick()
