from manim import *


class ManimCircle(MovingCameraScene):
    def construct(self):

        self.camera.background_color = '#ece6e2'

        numberPlane = NumberPlane()
        self.add(numberPlane)

        square = Square()
        circle = Circle()
        
        self.play(
            Transform(square, circle),
            subcaption="The square transforms."
        )


        triangle1 = Triangle()
        circle1 = Circle(radius=1,fill_color=WHITE).surround(triangle1).shift(LEFT * 2)
        p1 = circle1.point_at_angle(PI/2)
        p2 = circle1.point_at_angle(270 * DEGREES)
        s1 = Square(side_length = 0.25).move_to(p1)
        s2 = Square(side_length = 0.25).move_to(p2)

        line2 = Line(color=RED)
        circle2 = Circle(radius=1,color=BLACK,fill_color=BLACK).surround(line2,buffer_factor=2.0).shift(RIGHT * 2)
        circle3 = Circle(radius=4,fill_color=BLACK,fill_opacity=0.5)
        circle_group = Group(triangle1,circle1,s1,s2,line2,circle2,circle3).arrange(buff=1)

        self.play(FadeIn(circle_group,run_time = 1))
        self.play(FadeOut(circle_group,run_time = 1))

                
        arc1 = Arc(radius=2, start_angle=PI, angle=PI, color=WHITE).shift(LEFT * 2)
        arc2 = Arc(radius=2, start_angle=PI, angle=PI, color=WHITE).shift(RIGHT * 2)

        self.play(Create(arc1))
        self.play(Create(arc2))
   

        

        self.play(self.camera.frame.animate.scale(2))
        
