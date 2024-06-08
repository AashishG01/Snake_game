from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard ,Gameover
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    score.print_score()
    if (snake.head.xcor() < (food.xcor() + 10) and snake.head.xcor() > (food.xcor() - 10) and
            snake.head.ycor() < (food.ycor() + 10) and snake.head.ycor() > (food.ycor() - 10)):
        food.new_position()
        score.add_score()
        snake.extend()

    #creating a wall collision
    # print(snake.head.xcor())
    if ((snake.head.xcor() < 300 and snake.head.xcor() > 270) or (snake.head.xcor() > -300 and snake.head.xcor() < -270) or
            (snake.head.ycor() < 300 and snake.head.ycor() > 270) or (snake.head.ycor() > -300 and snake.head.ycor() < -270)):

        print("collison with wall")
        message = Gameover()
        game_is_on = False

    #detect collision with tail .

    for segment in  snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            message = Gameover()


screen.exitonclick()

