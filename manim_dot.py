#!./bin/python3

from manim import *

class ManimDot(Scene):
    def construct(self):
        dot1 = Dot(radius=1,color=BLUE,point=(1,1,1)).shift(RIGHT * 2)
        dot2 = Dot(radius=1,color=BLUE).shift(LEFT * 2)
        self.play(dot1.animate.move_to(LEFT * 2),run_time = 2)
        self.play(dot2.animate.move_to(RIGHT * 2),run_time = 2)


        pass

class MoveAlongPathExample(Scene):
    def construct(self):
        d1 = Dot(radius=0.5).set_color(ORANGE)
        l1 = Circle(radius= 1,color=RED)
        l2 = VMobject()
        self.add(d1, l1, l2)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(d1, l1), rate_func=linear)

