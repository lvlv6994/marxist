from manim import *

class Sword3D(ThreeDScene):
    def construct(self):
        # 创建剑的部分
        blade = self.create_blade()
        handle = self.create_handle()

        # 合并所有部分
        sword = VGroup(blade, handle)

        # 设置剑的位置
        sword.move_to(ORIGIN)

        # 显示剑
        self.play(Create(sword))

        # 动画效果：剑的旋转
        self.play(Rotate(sword, angle=2*PI, axis=UP, run_time=4))

        # 动画效果：剑的移动
        self.play(sword.animate.shift(RIGHT * 2))

        # 结束
        self.wait(2)

    def create_blade(self):
        # 剑刃部分（立方体）
        blade_body = Cube(side_length=0.1)
        blade_body.stretch_to_fit_height(4)
        blade_body.set_fill(GRAY, opacity=0.7)
        blade_body.set_stroke(WHITE, width=2)
        # 剑锋的部分（使用多边形）
        blade_edge = Polygon(
            *[
                [-0.05, -2.0, 0],
                [0.05, -2.0, 0],
                [0.0, 2.0, 0.05]
            ],
            color=GRAY
        )
        blade_edge.move_to(blade_body.get_top())

        # 将剑刃和剑锋组合起来
        blade = VGroup(blade_body, blade_edge)
        return blade

    def create_handle(self):
        # 剑柄部分（圆柱体）
        handle = Cylinder(radius=0.2, height=1, direction=UP)
        handle.move_to(ORIGIN + DOWN * 2.1)
        handle.set_fill(RED, opacity=0.9)
        handle.set_stroke(WHITE, width=2)
        return handle
