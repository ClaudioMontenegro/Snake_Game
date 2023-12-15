from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 14, 'bold')
FONT_OVER = ('Courier', 24, 'bold')

with open("data.txt") as data:
    data_score = int(data.read())


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 280)
        self.score = 0
        self.high_score = data_score
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(f"Score: {self.score}  Highest Score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def count_score(self):
        self.score += 1
        self.score_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
        self.score_board()
