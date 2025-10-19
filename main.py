import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Have Fun in My Snake Game!') ## window title

screen.tracer(0)
# turtle.tracer(n=None, delay=None)启用/禁用海龟动画并设置刷新图形的延迟时间。如果指定 n 值，则只有每第 n 次屏幕刷新会实际执行。


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.listen()


game_on = True
while game_on:
    screen.update() #should-be: body动一次，screen刷新一次
    time.sleep(0.08)

    snake.move()

    #detect collision: snake.head vs. food
    #turtle.distance(x, y=None) 返回从海龟位置到由 (x,y)，适量或另一海龟对应位置的单位距离
    ## head: 20x20; food: 10x10; distance:15=20/2+10/2
    if snake.head.distance(food) < 15.5:
        food.position_refresh()
        scoreboard.score_add()
        snake.extend_snake()

    # detect collision: snake.head vs. wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 265 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    # detect collision: snake.head vs. tail
    elif snake.tail_collision():
        game_on = False
        scoreboard.game_over()


screen.exitonclick()