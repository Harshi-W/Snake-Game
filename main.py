import time
from turtle import Screen
from Snake import Snake
from food import Food
from Score_board import Score

scr = Screen()
scr.setup(width=600, height=600)
scr.title("My Snake Game")
scr.bgcolor("black")
scr.tracer(0)

snake = Snake()
food = Food()
scoreb = Score()


scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")






game_off = False

while not game_off:
    scr.update()
    time.sleep(0.3)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreb.inc_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() <-280:
        scoreb.reset()
        snake.reset()


    for segments in snake.seg[1:]:
        if snake.head.distance(segments) < 10:
            scoreb.reset()
            snake.reset()
        else:
            pass





scr.exitonclick()








