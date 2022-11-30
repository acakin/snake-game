from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score} ", move=False, align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
        self.update_sb()

    def update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))

    def update_sb(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align='center', font=('Courier', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"      GAME OVER\nPress SPACE to restart", move=False,
                   align='center', font=('Courier', 24, 'bold'))
