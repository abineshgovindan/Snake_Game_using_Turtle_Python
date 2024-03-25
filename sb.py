from turtle import Turtle

class Score(Turtle):
    def __init__(self):



        super().__init__()
        self.score = 50
        self.hideturtle()
        self.up()
        self.goto((0, 270))
        self.color("white")
        self.score_update()

    def score_update(self):
        self.write(f"Score = {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto((0, 0))
        self.write(f"    Game Over \n Your final score = {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))



    def score_incres(self):
        self.score += 1
        self.clear()
        self.score_update()

