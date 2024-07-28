from manim import *

class MovingCube(Scene):
    def construct(self):
        # 创建立方体
        cube = Cube()

        # 设置立方体的颜色
        cube.set_fill(WHITE, opacity=0.5)
        cube.set_stroke(BLUE, width=2)

        # 显示立方体
        self.play(Create(cube))

        # 让立方体移动
        self.play(cube.animate.shift(RIGHT * 2))

        # 让立方体旋转
        self.play(cube.animate.rotate(PI / 4))

        # 结束
        self.wait(1)
