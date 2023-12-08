from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 12, 'bold')
FONT_OVER = ('Courier', 24, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 280)
        self.score = 0
        self.score_board()

    def score_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def count_score(self):
        self.score += 1
        self.clear()
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_OVER)