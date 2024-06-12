from manim import *

class DotWithPathMotion(Scene):
    def construct(self):
        # 创建一个圆形路径
        circle = Circle(radius=2, color=BLUE)

        # 创建一个点
        dot = Dot(radius = 1,color=RED)

        # 将圆形路径和点添加到场景中
        self.add(circle, dot)

        # 创建一个点沿着圆形路径运动的动画
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.wait(1)

# 运行这个 Scene 的命令是
# manim -pql script.py DotWithPathMotion
