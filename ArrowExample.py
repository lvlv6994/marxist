# from manim  import * 

# class ArrowExample(Scene):
#       def construct(self):
#           arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
#           arrow_2 = Arrow(start=RIGHT, end=LEFT, color=GOLD, tip_shape=ArrowSquareTip).shift(DOWN)
#           g1 = Group(arrow_1, arrow_2)

#           # the effect of buff
#           square = Square(color=MAROON_A)
#           arrow_3 = Arrow(start=LEFT, end=RIGHT)
#           arrow_4 = Arrow(start=LEFT, end=RIGHT, buff=0).next_to(arrow_1, UP)
#           g2 = Group(arrow_3, arrow_4, square)

#           # a shorter arrow has a shorter tip and smaller stroke width
#           arrow_5 = Arrow(start=ORIGIN, end=config.top).shift(LEFT * 4)
#           arrow_6 = Arrow(start=config.top + DOWN, end=config.top).shift(LEFT * 3)
#           g3 = Group(arrow_5, arrow_6)

#           self.add(Group(g1, g2, g3).arrange(buff=2))


from manim import *

class StylishObjectsArrowExample(Scene):
    def construct(self):
        # 创建两个圆形
        circle1 = Circle().shift(LEFT * 2)
        circle2 = Circle().shift(RIGHT * 2)

        # 创建一个从第一个圆形到第二个圆形的箭头
        arrow = Arrow(
            circle1.get_center(), 
            circle2.get_center(), 
            color=RED, 
            stroke_width=8, 
            tip_length=0.5,
            tip_shape=ArrowTriangleTip
        )

        # 添加发光效果
        glowing_arrow = VGroup(
            arrow.copy().set_stroke(color=RED, width=12, opacity=0.5),
            arrow.copy().set_stroke(color=RED, width=20, opacity=0.2),
            arrow.copy().set_stroke(color=RED, width=30, opacity=0.1),
            arrow
        )

        # 显示圆形和箭头
        self.play(Create(circle1), Create(circle2), Create(glowing_arrow))
        self.wait(2)
          
