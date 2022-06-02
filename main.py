from turtle import Turtle, Screen
import time
from Scoreboard import Scoreboard
from Snake import Snake
from Food import Food

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaking")
screen.tracer(0)

#instances
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#keystrokes
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    # screen.delay(1)
    snake.move()

    #collision between snake and food
    if (snake.snake[0].distance(food) < 15):
        food.refresh()
        snake.extend()
        scoreboard.add_score()
        scoreboard.update_text()

    #collision between snake and wall
    if (snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280):
        scoreboard.game_over()
        game_on = False

    #Detect collision with tail.
    for snake_body in snake.snake:
        if snake_body == snake.snake[0]:
            pass
        elif snake.snake[0].distance(snake_body) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()