from manim import *

class MovingText3D(ThreeDScene):
    def construct(self):
        # 创建 3D 文本
        text = Text("3D Text", font_size=72, weight=BOLD)

        # 将文本设置为 3D
        text3d = text.copy().shift(OUT)  # 使用 `OUT` 将文本从视图稍微推开，给出 3D 效果

        # 设置文本的颜色
        text.set_color(WHITE)
        text3d.set_color(BLUE)

        # 显示文本
        self.play(Create(text))
        self.play(Create(text3d))

        # 动画：旋转文本
        self.play(
            Rotate(text, angle=2*PI, axis=UP),
            Rotate(text3d, angle=2*PI, axis=RIGHT),
            run_time=4
        )

        # 动画：文本向前移动
        self.play(text.animate.shift(OUT * 2))
        self.play(text3d.animate.shift(OUT * 2))

        # 结束
        self.wait(2)
