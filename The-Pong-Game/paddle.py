from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cords):
        super().__init__()
        self.cords = cords
        self.shape("square")
        # 1 = 20px
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.color("white")
        self.penup()
        if self.cords[0] == 350:
            self.goto(350, 0)
        elif self.cords[0] == -350:
            self.goto(-350, 0)
        else:
            print("An error has occurred")

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
