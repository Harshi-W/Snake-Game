from turtle import Turtle

LIST1 = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]

    def create_snake(self):
        for pos in LIST1:
            self.add_segment(pos)


    def add_segment(self, pos):
        newt = Turtle("square")
        newt.color("white")
        newt.penup()
        newt.goto(pos)
        self.seg.append(newt)

    def reset(self):
        for segments in self.seg:
            segments.goto(1000, 1000)
        self.seg.clear()
        self.create_snake()
        self.head = self.seg[0]



    def extend(self):
        self.add_segment(self.seg[-1].position())


    def move(self):
        for seg_num in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[seg_num - 1].xcor()
            new_y = self.seg[seg_num - 1].ycor()
            self.seg[seg_num].goto(new_x, new_y)

        self.seg[0].forward(MOVE_DIS)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
