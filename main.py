from turtle import Turtle, Screen
import time
import turtle
from Scoreboard import Scoreboard
from Snake import Snake
from Food import Food

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaking")

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
    # time.sleep(0.1)
    screen.delay(1)
    snake.move()

    #collision between snake and food
    if (snake.snake[0].distance(food) < 15):
        food.refresh()
        scoreboard.add_score()
        scoreboard.update_text()

    #collision between snake and wall
    if (snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280):
        scoreboard.game_over()
        game_on = False

screen.exitonclick()