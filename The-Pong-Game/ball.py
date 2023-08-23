from turtle import Turtle

SPEED_LEVELS = ["slow", "normal", "fast", "fastest"]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed(1)
        self.x_move = 10
        self.y_move = 10
        self.r_score = 0
        self.l_score = 0
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.l_score += 1
        self.setpos(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
