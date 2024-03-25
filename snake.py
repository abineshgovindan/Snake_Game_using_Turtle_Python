import turtle as t
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

snak_len = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
class Snake():

    def __init__(self):
        self.seg = []
        self.creat()
        self.head = self.seg[0]


    def creat(self):
        for i in snak_len:
            self.add_seg(i)





    def add_seg(self,position):
        snake = t.Turtle(shape="square")
        snake.color("white")
        snake.up()
        snake.goto(position)
        self.seg.append(snake)

    def extend(self):
        self.add_seg(self.seg[-1].position())




    def move(self):
        for n in range(len(self.seg) - 1, 0, -1):
            n_x = self.seg[n - 1].xcor()
            n_y = self.seg[n - 1].ycor()
            self.seg[n].goto(n_x, n_y)
        self.seg[0].forward(MOVE)

    def Up(self):
        if self.seg[0].heading() != DOWN :
            self.seg[0].setheading(90)

    def Down(self):
        if self.seg[0].heading() != UP:
            self.seg[0].setheading(270)

    def Right(self):
        if self.seg[0].heading() != LEFT:
            self.seg[0].setheading(0)

    def Left(self):
        if self.seg[0].heading() != RIGHT:

         self.seg[0].setheading(180)



