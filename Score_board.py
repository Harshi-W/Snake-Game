from turtle import Turtle



class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        with open("data.txt") as file:
            contents = int(file.read())
            self.high_score = contents
            file.close()
        self.up_score()

    def up_score(self):
        self.write(f"Score:{self.score}, High score: {self.high_score}",  align="center", font=('Arial', 8, 'normal'))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0

        self.up_score()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("white")
    #     self.write("Game over", align='center',font=('Arial', 12, 'normal') )


    def inc_score(self):
        self.score += 1
        self.clear()
        self.up_score()

