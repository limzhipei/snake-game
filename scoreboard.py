from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode='r') as data_file:
            self.high_score = int(data_file.read())
        self.ht()
        self.up()
        self.color("white")
        self.goto(-150, 280)
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data_file:
                data_file.write(f"{self.high_score}")
            self.score = 0
            self.clear()
            self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        else:
            self.score = 0
            self.clear()
            self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)



