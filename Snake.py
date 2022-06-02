from turtle import Turtle

initial_position = [(0,0),(-20,0),(-40,0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():
    def __init__(self):
        #snake
        self.snake = []

        for i in range(3):
            snake_body = Turtle("square")
            snake_body.penup()
            snake_body.color("white")
            snake_body.goto(initial_position[i])        
            self.snake.append(snake_body)

    def move(self):
        for i in range(len(self.snake)-1,0,-1):
            xcor = self.snake[i-1].xcor()
            ycor = self.snake[i-1].ycor()
            self.snake[i].goto(xcor,ycor)
        self.snake[0].forward(20)

    def up(self):
        if (self.snake[0].heading() != DOWN):
            self.snake[0].setheading(UP)

    def left(self):
        if (self.snake[0].heading() != RIGHT):
            self.snake[0].setheading(LEFT)

    def down(self):
        if (self.snake[0].heading() != UP):
            self.snake[0].setheading(DOWN)

    def right(self):
        if (self.snake[0].heading() != LEFT):
            self.snake[0].setheading(RIGHT)
