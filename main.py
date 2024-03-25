from turtle import Turtle, Screen
import time
from sb import Score
from food import Food
from snake import Snake
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.colormode(255)
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_obj = Score()



screen.listen()
# screen.onkey(snake.Up,"Up")
# screen.onkey(snake.Down,"Down")
# screen.onkey(snake.Right,"Right")
# screen.onkey(snake.Left,"Left")
screen.onkey(snake.Up,"W")
screen.onkey(snake.Down,"S")
screen.onkey(snake.Right,"D")
screen.onkey(snake.Left,"A")








game = True

while game:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("food")
        snake.extend()
        food.refresh()
        score_obj.score_incres()
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game =False
        score_obj.game_over()

    for seg in snake.seg[1:]:


        if snake.head.distance(seg) <10:
             game = False
             score_obj.game_over()










screen.exitonclick()











