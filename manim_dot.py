#!./bin/python3

from manim import *

class ManimDot(Scene):
    def construct(self):
        text = Text('z_index = 3', color = PURE_RED).shift(UP).set_z_index(3)
        square = Square(2, fill_opacity=1).set_z_index(2)
        tex = Tex(r'zIndex = 1',color = PURE_BLUE).shift(DOWN).set_z_index(1)
        circle = Circle(radius = 1.7, color = GREEN, fill_opacity = 1)

        self.add(text)
        self.add(square)
        self.add(tex)
        self.add(circle)
        
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




        
