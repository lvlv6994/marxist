from manim import *
class ManimCircle(Scene):
    def construct(self):
#        circle = Circle(radius=2,fill_color=WHITE,fill_opacity=1)
#        self.add(circle)
        numberPlane = NumberPlane()
        self.add(numberPlane)
        circle1 = Circle(radius=1,fill_color=WHITE).shift(LEFT * 2)
        circle2 = Circle(radius=1,color=BLACK,fill_color=BLACK).shift(RIGHT * 2)
        circle3 = Circle(radius=4,fill_color=BLACK,fill_opacity=0.5)
        arc1 = Arc(radius=2, start_angle=PI, angle=PI, color=WHITE).shift(LEFT * 2)
        arc2 = Arc(radius=2, start_angle=PI, angle=PI, color=WHITE).shift(RIGHT * 2)

        self.play(Create(circle1))
        self.play(Create(circle2))
        self.play(Create(circle3))
        self.play(Create(arc1))
        self.play(Create(arc2))

        
