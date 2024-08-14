from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        #self.play(FadeOut(square))  # fade out animation

class FormBigSquare(Scene):
    def construct(self):
        big_square = Square(side_length=7)
        s0 =  Square(side_length=5);
        s0.rotate(PI/4)

        s1 =  Square(side_length=4);
        s2 =  Square(side_length=3);

        


        self.play(Create(big_square))
        self.play(Create(s0))
        sleep(5)
        self.play(Create(s1))
        self.play(Create(s2))
        self.play(Transform(s0,s1))
